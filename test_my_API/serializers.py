from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Item, UserRegistration, CharityRegistration, OrderItem

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields  = ['ItemId', 'ItemName', 'Quantity', 'Cat', 'Charity']


class ItemOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields  = ['ItemId', 'ItemName', 'Quantity', 'Username']


class CharityRegistrationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CharityRegistration
        fields = ['Email', 'CharityName', 'Password', 'City']

class CharityLoginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CharityRegistration
        fields = ['Email', 'Password']

class CharityGetAllSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CharityRegistration
        fields = ['Email', 'CharityName', 'City']

class UserRegistrationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserRegistration
        fields = ['Email', 'Username', 'CharityName', 'Password', 'City']

class UserLoginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserRegistration
        fields = ['Email', 'Password']