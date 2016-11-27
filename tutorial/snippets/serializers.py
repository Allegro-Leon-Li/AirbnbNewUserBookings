from rest_framework import serializers
# from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from snippets.models import Users


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'account', 'email', 'age', 'language', 'os', 'browser', 'location')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('location',)
