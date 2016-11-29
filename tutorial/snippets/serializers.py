from rest_framework import serializers
# from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from snippets.models import Users, UsersLocation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'account', 'email', 'gender', 'age', 'language', 'os', 'browser', 'location')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersLocation
        fields = ('account', 'location_1', 'location_2', 'location_3', 'location_4', 'location_5')
