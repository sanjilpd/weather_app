from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('next1/', views.index1),
    path('next2/', views.index2)
]
