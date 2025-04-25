from . import models
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import ValidationError
import re


class LocationSerializer(ModelSerializer):
    class Meta:
        model = models.Location
        fields = (
            'id', 'lat', 'lon', 'address', 'description', 'region'
        )


class PartnerApplicationObjectSerializer(ModelSerializer):

    location = LocationSerializer(write_only=True)

    class Meta:
        model = models.PartnerApplicationObject
        fields = (
            'id', 'type', 'floor', 'area', 'price', 'rent', 'location'
        )

    def create(self, validated_data):
        location_data = validated_data.pop('location')
        location = models.Location.objects.create(**location_data)
        validated_data['location'] = location

        return super().create(validated_data)


class CategorySerializer(ModelSerializer):

    class Meta:
        model = models.Category
        fields = (
            'id','name', 'order'
        )


class ProductSerializer(ModelSerializer):

    class Meta:
        model = models.Product
        fields = (
            'id' ,'name', 'image', 'description', 'price', 'category'
        )


class CategoryProductMixedSerializer(ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = models.Category
        fields = (
            'id', 'name', 'order', 'products'
        )


class NewSerializer(ModelSerializer):

    class Meta:
        model = models.New
        fields = (
            'id', 'title', 'poster', 'body', 'created_at'
        )


class AboutUsSerializer(ModelSerializer):

    class Meta:
        model = models.AboutUs
        fields = (
                'id', 'key', 'value'
        )



class UserEmailSerializer(ModelSerializer):

    class Meta:
        model = models.UserEmail
        fields = (
            'id', 'email'
        )


class FeedbackSerializer(ModelSerializer):

    class Meta:
        model = models.Feedback
        fields = (
            'id', 'full_name', 'text', 'source'
        )


class FAQSerializer(ModelSerializer):

    class Meta:
        model = models.FAQ
        fields = (
            'id', 'question', 'answer'
        )


class BranchSerializer(ModelSerializer):

    class Meta:
        model = models.Branch
        fields = (
            'id', 'name', 'order', 'image', 'duration', 'address', 'lat', 'lon'
        )


class UserSerializer(ModelSerializer):

    class Meta:
        model = models.User
        fields = (
            'id', 'full_name', 'phone'
        )

    def validate_phone(self, phone):
        pattern = r'^\+998(99|88|33|91|90|94|93)\d{7}$'
        if not re.match(pattern, phone):
            raise ValidationError({"phone": "Phone incorrect"})
        return phone


class UserLocationSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = models.UserLocation
        fields = (
            'id', 'lat', 'lon', 'address', 'user'
        )


class UserCardSerializer(ModelSerializer):

    class Meta:
        model = models.UserCard
        fields = (
            'id', 'user', 'card_ud', 'card_en', 'description', 'status'
        )


class VacancySerializer(ModelSerializer):

    class Meta:
        model = models.Vacancy
        fields = (
            'id', 'title', 'description', 'body'
        )


class VacancyApplicationSerializer(ModelSerializer):

    class Meta:
        model = models.VacancyApplication
        fields = (
            'id', 'full_name', 'phone', 'cv', 'vacancy'
        )

    def validate_phone(self, phone):
        pattern = r'^\+998(99|88|33|91|90|94|93)\d{7}$'
        if not re.match(pattern, phone):
            raise ValidationError({"phone": "Phone incorrect"})
        return phone


class VacancyVacancyApplicationMixedSerializer(ModelSerializer):
    vacancy_applications = VacancyApplicationSerializer(many=True)

    class Meta:
        model = models.Vacancy
        fields = (
            'id', 'title', 'description', 'body','vacancy_applications'
        )



class CareerSerializer(ModelSerializer):

    class Meta:
        model = models.Career
        fields = (
            'id', 'photo', 'text'
        )


class OrderSerializer(ModelSerializer):

    class Meta:
        model = models.Order
        fields = (
            'id', 'amount', 'status'
        )



class OrderProductSerializer(ModelSerializer):
    class Meta:
        model = models.OrderProduct
        fields = (
            'id', 'product', 'order', 'amount'
        )


class OrderOrderProductMixedSerializer(ModelSerializer):
    order_products = ProductSerializer(source='product')
    orders = OrderSerializer(source='order')

    class Meta:
        model = models.OrderProduct
        fields = ('id', 'order', 'product', 'amount', 'order_products', 'orders')


class CertificateSerializer(ModelSerializer):

    class Meta:
        model = models.Certificate
        fields = (
            'id', 'title', 'image'
        )



