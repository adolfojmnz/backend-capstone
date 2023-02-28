from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/', include('restaurant.urls')),

    path('api/token/login', TokenObtainPairView.as_view()),
    path('api/token/refresh', TokenRefreshView.as_view()),

    path('api/auth/', include('djoser.urls')),
]
