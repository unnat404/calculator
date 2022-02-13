# added Unnat

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Client

# User Serializer
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        # fields = ('id', 'username', 'email')
        fields = '__all__'

# # Register Serializer
# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Client
#         fields = ('id', 'username', 'email', 'password')
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         user = Client.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
#         #above will give error as originally it was giving for User model(inbuilt)

#         return user


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'first_name', 'last_name', 'email', 'profile_pic', 'address')
        # fields = ('id', 'first_name', 'last_name', 'email', 'password', 'profile_pic', 'address')
        # extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Client.objects.create_user(validated_data['first_name'], validated_data['email'], validated_data['password'])
        #above will give error as originally it was giving for User model(inbuilt)

        return user

