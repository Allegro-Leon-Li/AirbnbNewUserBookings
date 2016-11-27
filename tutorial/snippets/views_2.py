
# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from snippets.models import Users
from snippets.serializers import UserSerializer
from django.shortcuts import render

renderer_classes = [TemplateHTMLRenderer]
template_name = 'index.html'


def index(request):
    test_list = Users.objects.all()
    context = {'test_list': test_list}
    return render(request, 'snippets/index.html', context)

@api_view(['GET', 'POST'])
def user_list(request, format=None):
    """
    List all users, or create a new user.
    """
    if request.method == 'GET':
        users = Users.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        test_list = Users.objects.all()
        context = {'test_list': test_list}
        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return render(request, 'snippets/index.html', context)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk, format=None):
    """
    Retrieve, update or delete a user instance.
    """
    try:
        user = Users.objects.get(pk=pk)
    except Users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def loc_detail(request, pk, format=None):
    """
    Retrieve, update or delete a user instance.
    """
    try:
        user = Users.objects.get(pk=pk)
    except Users.DoesNotExist:
        return Response('error',status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data.get('location'))
        # return HttpResponse(
        #     json.dumps("ss"),
        #     content_type="application/json"
        # )