
from django.urls import path, include
from rest_framework import routers
from .api import GeolocationViewset
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .auth import RegisterView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'locations', GeolocationViewset, basename='locations')


urlpatterns = [
    path('auth/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/signup', RegisterView.as_view()),
]

urlpatterns += router.urls
