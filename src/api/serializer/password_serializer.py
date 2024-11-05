from user.models.user_model import UserModel
from rest_framework.serializers import ModelSerializer


class PasswordSerializer(ModelSerializer):

    class Meta:
        model = UserModel
        fields = ["password"]