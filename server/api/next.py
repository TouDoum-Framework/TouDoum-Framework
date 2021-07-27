from django.http import HttpRequest
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from server.api.serializers import *


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


def nextBrowsableAPI(request: HttpRequest):
    return render(request, 'browsable.html')
