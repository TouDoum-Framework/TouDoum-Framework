from django.urls import path
from server.modules.src.example import views

url_api = [
    path('test', views.test)
]
url_panel = []
