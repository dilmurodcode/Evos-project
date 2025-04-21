from rest_framework import generics
from . import models
from . import serializers
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


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
    queryset = models.Category.objects.all().order_by('order')
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