from rest_framework_simplejwt.views import TokenObtainPairView


class BaseTokenObtainPairView(TokenObtainPairView):
    serializer_class = BaseTokenObtainPairSerializer