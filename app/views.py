from rest_framework import generics
from .models import *
from rest_framework.response import Response
from . import serializers

class ApplicationObjectCreateAPIView(generics.CreateAPIView):
    queryset = PartnerApplicationObject.objects.all()
    serializer_class = serializers.PartnerApplicationObjectSerializer

    def post(self, request, *args, **kwargs):
        serializer= self.serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)

        instance = serializer.save()

        return Response('success')



