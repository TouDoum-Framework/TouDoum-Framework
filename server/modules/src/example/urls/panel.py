from django.urls import path
from server.modules.src.example import views

urlpatterns = [
    path('', views.test, name="test"),
]
