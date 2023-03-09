#create routes for the serializers token routes

from django.urls import path, include
from . import views
from .views import MyTokenObtainPairView

#from the simpleJWT authentication
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('', views.getRoutes),

    path('tickers/', views.tickers),

    #from the simpleJWT authentication
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'), #takes in the username and password to give an authentication and refresh token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), #takes in the refresh token -> gives a new refresh token
]