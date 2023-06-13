from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import status
from .models import CustomUser
from .serializers import CustomUserSerializer, CustomTokenObtainPairSerializer, CustomTokenRefreshSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class=CustomTokenObtainPairSerializer
    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.user
        
        access_token, refresh_token=user.get_tokens_for_user()
        response_data={
            'access_token':access_token,
            'refresh_token':refresh_token,
            'user_id':user.id
        }
        return Response(response_data, status=status.HTTP_200_OK)
    
class CustomTokenRefreshView(TokenRefreshView):
    serializer_class=CustomTokenRefreshSerializer
    
    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user=request.user
        
        access_token=serializer.validated_data['access']
        refresh_token=serializer.validated_data['refresh']
        
        response_data={
            'access_token': str(access_token),
            'refresh_token':str(refresh_token),
            'user_id':user.id
        }
        
        return Response(response_data, status=status.HTTP_200_OK)