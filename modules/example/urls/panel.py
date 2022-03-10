from django.urls import path
from modules.example import views

urlpatterns = [
    path('', views.test, name="test"),
]
