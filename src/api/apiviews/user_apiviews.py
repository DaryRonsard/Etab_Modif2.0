from django.db.migrations import serializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status, mixins
from rest_framework.decorators import action
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password

from user.models.user_model import UserModel
from api.serializer.user_serializer import UserSerializer
from rest_framework import filters
from api.serializer.password_serializer import PasswordSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()

    # hacher le mots de passe lors de la creations
    @action(detail=False, methods=['post'])
    def create_crypt_and_password(self, request, pk=None):
        data = JSONParser().parse(request)
        password = data['password']
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save(password=make_password(password))
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


    #@action(detail=False, methods=['post'])
    @action(detail=True, methods=['put'], url_path='change_password')
    def change_password(self, request, pk=None):
        user = self.get_object()
        serializer = PasswordSerializer(
            data=request.data)  # Utiliser uniquement pour valider les données du mot de passe

        if serializer.is_valid():  # Valider les données
            new_password = serializer.validated_data['password']  # Récupère le mot de passe validé
            user.password = make_password(new_password)  # Hacher et mettre à jour le mot de passe
            user.save()  # Sauvegarder l'utilisateur avec le nouveau mot de passe
            return Response({'detail': 'Mot de passe changé avec succès !'}, status=status.HTTP_200_OK)

        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #update
    # @action(detail=True, methods=['PUT'], url_path='change_password', serializer_class=PasswordSerializer)
    # def update_password(self, request, pk=None):
    #     user = self.get_object()
    #     serializer = PasswordSerializer(user, data=request.data)
    #     if serializer.is_valid():
    #         user.password = make_password(serializer.validated_data['password'])
    #         serializer.save()
    #         return Response({'detail': 'Mot de passe changé avec succès !'}, status=201)
    #     return JsonResponse(serializer.errors, status=400)


'''
def user_list(request):
    if request.method == 'GET':
        user = UserModel.objects.all()
        serializer = UserSerializer(user, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def user_detail(request, pk):
    try:
        user = UserModel.objects.get(pk=pk)
    except UserModel.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        user = UserModel.objects.get(pk=pk)
        user.delete()
        return HttpResponse(status=204)
'''

# class UserListView(generics.ListAPIView):
#     queryset = UserModel.objects.all()
#     serializer_class = UserSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['username', 'email']
