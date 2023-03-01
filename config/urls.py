from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('restaurant.urls')),

    path('api/token/login/', TokenObtainPairView.as_view(), name='token-login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),

    path('auth/', include('djoser.urls')),
]
