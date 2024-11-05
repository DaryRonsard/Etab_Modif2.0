from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser

from api.serializer.adress_serializer import AdressSerializer
from base.models.address_model import AddressModel


class AdressViewSet(viewsets.ModelViewSet):
    queryset = AddressModel.objects.all()
    serializer_class = AdressSerializer
    