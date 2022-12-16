from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('products/', views.myProducts),
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
