from rest_framework import serializers
from django.contrib.auth.models import User


# TODO:_ add password hashing

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
