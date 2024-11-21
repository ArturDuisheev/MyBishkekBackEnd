from djoser.serializers import UserSerializer, User
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField


class ProfileSerializer(UserSerializer):
    phone_number: str = PhoneNumberField(region='KG')
    car_number: str = serializers.CharField(min_length=7, max_length=10)
    fullname: str = serializers.CharField(max_length=30)

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'phone_number', 'car_number', 'fullname')
