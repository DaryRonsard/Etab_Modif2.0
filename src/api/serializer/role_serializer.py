from rest_framework import serializers

from user.models.role_user_model import RoleUserModel


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleUserModel
        exclude = '__all__'
