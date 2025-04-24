import re

from rest_framework import generics
from . import models
from . import serializers
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


class ApplicationObjectCreateAPIView(generics.CreateAPIView):
    queryset = models.PartnerApplicationObject.objects.all()
    serializer_class = serializers.PartnerApplicationObjectSerializer

    def post(self, request, *args, **kwargs):
        serializer= self.serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)

        instance = serializer.save()

        return Response('success')


class CategoryAPIView(generics.ListAPIView):
    queryset = models.Category.objects.all().order_by('order')
    serializer_class = serializers.CategorySerializer


class ProductAPIView(generics.ListAPIView):
    serializer_class = serializers.ProductSerializer
    pagination_class = None

    def get_queryset(self):
        category = self.request.query_params.get('category', None)
        queryset = models.Product.objects.all()

        if category and category.isdigit():
            queryset = queryset.filter(category=category)

        return queryset


class CategoryProductMixedAPIView(generics.ListAPIView):
    queryset = models.Category.objects.all().prefetch_related('products')
    serializer_class = serializers.CategoryProductMixedSerializer
    pagination_class = None


class NewAPIWView(generics.ListAPIView):
    queryset = models.New.objects.all().order_by('-created_at')
    serializer_class = serializers.NewSerializer
    permission_classes = [AllowAny]


class AboutUsAPIView(generics.ListAPIView):
    queryset = models.AboutUs.objects.all()
    serializer_class = serializers.AboutUsSerializer


class UserEmailAPIView(generics.CreateAPIView):
    queryset = models.UserEmail.objects.all()
    serializer_class = serializers.UserEmailSerializer

    def post(self, request, *args, **kwargs):
        email = serializers.UserEmailSerializer(data=request.data)
        if email.is_valid():
            email.save()
            return Response(
                data={'email': 'UserEmail create success'},
                status=201
            )
        return Response('email error')



class FeedbackAPIView(generics.ListAPIView):
    queryset = models.Feedback.objects.all()
    serializer_class = serializers.FeedbackSerializer


class FAQAPIView(generics.ListCreateAPIView):
    queryset = models.FAQ.objects.all()
    serializer_class = serializers.FAQSerializer



class BranchAPIView(generics.ListAPIView):
    serializer_class = serializers.BranchSerializer


    def get_queryset(self):
        name = self.request.query_params.get('name', None)
        kw = {"name": name} if name else {}
        return models.Branch.objects.filter(**kw).order_by('-order')



class UserCreateAPIView(generics.CreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

    def post(self, request, *args, **kwargs):
        full_name = self.request.data.get('full_name')

        if not re.fullmatch(r"[A-Za-zÀ-ÿ\s'-]+", full_name):
            return Response(
                data={"full_name": "Full_name incorrect"},
                status=400
            )
        return super().post(request, *args, **kwargs)


class UserLocationAPIView(generics.ListAPIView):
    queryset = models.UserLocation.objects.all().select_related('user')
    serializer_class = serializers.UserLocationSerializer


class UserCardAPIView(generics.ListAPIView):
    queryset = models.UserCard.objects.all()
    serializer_class = serializers.UserCardSerializer


class VacancyAPIView(generics.ListAPIView):
    queryset = models.Vacancy.objects.all()
    serializer_class = serializers.VacancySerializer


class VacancyApplicationAPIView(generics.CreateAPIView):
    queryset = models.VacancyApplication.objects.all()
    serializer_class = serializers.VacancyApplicationSerializer

    def post(self, request, *args, **kwargs):
        full_name = self.request.data.get('full_name')

        if not re.fullmatch(r"[A-Za-zÀ-ÿ\s'-]+", full_name):
            return Response(
                data={"full_name": "Full name incorrect"},
                status=400
            )
        return super().post(request, *args, **kwargs)


class VacancyVacancyApplicationMixedAPIView(generics.ListAPIView):
    queryset = models.Vacancy.objects.all().prefetch_related('vacancy_applications')
    serializer_class = serializers.VacancyVacancyApplicationMixedSerializer



class CareerAPIView(generics.ListAPIView):
    queryset = models.Career.objects.all()
    serializer_class = serializers.CareerSerializer


class OrderProductAPIView(generics.ListAPIView):
    queryset = models.Order.objects.all().prefetch_related('order')
    serializer_class = serializers.OrderProductSerializer


class CertificateAPIView(generics.ListAPIView):
    queryset = models.Certificate.objects.all().order_by('-id')
    serializer_class = serializers.CertificateSerializer