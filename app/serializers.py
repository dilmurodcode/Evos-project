from . import models
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = (
            'id','name', 'order'
        )


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Product
        fields = (
            'id' ,'name', 'image', 'description', 'price', 'category'
        )


class CategoryProductMixedSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = models.Category
        fields = (
            'id', 'name', 'order', 'products'
        )


    def get_products(self, obj):
        queryset = models.Product.objects.filter(
            category=obj
        )
        serializer = ProductSerializer(queryset, many=True)
        return serializer.data


class NewSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.New
        fields = (
            'id', 'title', 'poster', 'body'
        )


class AboutUsSerializer(serializers.ModelSerializer):
    model = models.AboutUs
    field = (
        'id', 'title', 'poster', 'body'
    )


class FAQSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.FAQ
        fields = (
            'id', 'question', 'answer'
        )


class AboutU(serializers.ModelSerializer):
    model = models.AboutUs
    fields = (
        'id', 'key', 'value'
    )
