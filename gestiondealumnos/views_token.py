from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers_token import TokenSerializer


class TokenView(TokenObtainPairView):
    serializer_class = TokenSerializer
