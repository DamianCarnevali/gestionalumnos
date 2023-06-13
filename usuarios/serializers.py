from rest_framework import serializers
from .models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'nombre', 'apellido', 'password',
                  'is_active', 'is_staff', 'is_superuser']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def get_token(cls,user):
        token=super().get_token(user)
        return token
    
class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self,attrs):
        data=super().validate(attrs)
        data['user_id']=self.context['request'].user.id
        return data