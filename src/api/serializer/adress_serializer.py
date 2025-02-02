from rest_framework import serializers

from base.models.address_model import AddressModel


class AdressSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressModel
        fields = '__all__'