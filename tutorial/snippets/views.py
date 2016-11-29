from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from snippets.models import Users
from snippets.serializers import UserSerializer, LocationSerializer
from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.permissions import IsAdminUser

renderer_classes = [TemplateHTMLRenderer]
template_name = 'index.html'


def index(request):
    test_list = Users.objects.all()
    context = {'test_list': test_list}
    return render(request, 'snippets/index.html', context)


def login(request):
    test_list = Users.objects.all()
    context = {'test_list': test_list}
    return render(request, 'snippets/login.html', context)


class UserList(generics.ListCreateAPIView):
    model = Users
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class UserDetail(generics.RetrieveAPIView):
    model = Users
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class LocationDetail(generics.RetrieveAPIView):
    model = Users
    queryset = Users.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [
        permissions.AllowAny
    ]
