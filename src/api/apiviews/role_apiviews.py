from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser

from api.serializer.role_serializer import RoleSerializer
from user.models.role_user_model import RoleUserModel


class RoleViewSet(viewsets.ModelViewSet):
    serializer_class = RoleSerializer
    queryset = RoleUserModel.objects.all()