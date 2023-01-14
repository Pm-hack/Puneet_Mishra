from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('generate-otp/', views.requestOtp),
    path('verify-otp/', views.verifyOtp),
]

