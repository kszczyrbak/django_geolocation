from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Geolocation


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        return User.objects.create_user(
            validated_data['username'],
            password=validated_data['password'],
        )


class GeolocationPostSerializer(serializers.Serializer):

    hostname = serializers.CharField(max_length=255, required=True)

    def create(self, validated_data):
        return {
            'host': validated_data["host"]
        }


class GeolocationSerializer(serializers.ModelSerializer):

    hostname = serializers.CharField(max_length=255, required=True)

    class Meta:
        model = Geolocation
        fields = '__all__'

    def create(self, validated_data):
        return Geolocation.objects.create(**validated_data)
