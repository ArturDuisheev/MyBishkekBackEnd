from djoser.serializers import UserSerializer, User
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField


class ProfileSerializer(UserSerializer):
    phone_number: str = PhoneNumberField(region='KG')
    fullname: str = serializers.CharField(max_length=30)
    car_model: str = serializers.CharField(max_length=120)
    license_plate_number: str = serializers.CharField(min_length=7, max_length=10)
    vin_code: str = serializers.CharField(min_length=17, max_length=17)
    year_of_manufacture: int = serializers.IntegerField(min_value=1980, max_value=2024)

    class Meta:
        model = User
        fields = ('id',
                  'email',
                  'username',
                  'phone_number',
                  'fullname',
                  'car_model',
                  'license_plate_number',
                  'vin_code',
                  'year_of_manufacture'
                  )
