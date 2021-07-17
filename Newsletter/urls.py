"""Newsletter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from Categoria.views import CategoriaListView
from django.contrib import admin
from django.urls import path, include
from Boletin.views import BoletinListView, BoletinViewsDetail, VotacionListView, VotacionViewsDetail
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # -- ENDPOINT PARA BOLETINES --
    # GET, PUT, DELETE
    path('api/v1/boletin/<int:pk>', BoletinViewsDetail.as_view()),
    path('api/v1/boletin/', BoletinListView.as_view()),  # GET as List - POST
    # -- ENDPOINTS FOR VOTACIONES --
    # GET, PUT, DELETE
    path('api/v1/votacion/<int:pk>', VotacionViewsDetail.as_view()),
    path('api/v1/votacion/', VotacionListView.as_view()),  # GET as List - POST
    # -- ENDPOINT PARA CATEGORIAS --
    path('api/v1/categoria/', CategoriaListView.as_view())


]
