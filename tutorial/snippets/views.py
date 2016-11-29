from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from snippets.models import Users, UsersLocation
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


def test(request):
    return render(request, 'snippets/location.html')


def result(name):
    test_list = Users.objects.all()
    context = {'test_list': test_list}
    location_data_save = ['us', 'de', 'fr', 'ot', 'au']
    serializer_loc = LocationSerializer(
        data={'account': name, 'location_1': location_data_save[0], 'location_2': location_data_save[1],
              'location_3': location_data_save[2], 'location_4': location_data_save[3],
              'location_5': location_data_save[4]})
    if serializer_loc.is_valid():
        serializer_loc.save()
        return True
    return False


class UserList(generics.ListCreateAPIView):
    model = Users
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    def perform_create(self, serializer):
        serializer.save()
        print(result(self.request.data['account']))
        # print(self.request.data['account'])


class UserDetail(generics.RetrieveAPIView):
    model = Users
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'account'
    permission_classes = [
        permissions.AllowAny
    ]


class LocationDetail(generics.RetrieveAPIView):
    model = UsersLocation
    queryset = UsersLocation.objects.all()
    lookup_field = 'account'
    serializer_class = LocationSerializer
    permission_classes = [
        permissions.AllowAny
    ]


# Temporary function for demo of sprint3
# TODO: use user's authorization method and session to render index.html
# This method is to be dropped in sprint 4
def userinfo(request, account):
    test_list = Users.objects.all()
    context = {'test_list': test_list, 'username': account}
    return render(request, 'snippets/index.html', context)
