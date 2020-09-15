from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Point, DateCount


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username',)

class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = '__all__'

class PointListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Point
        fields = '__all__'

class DailySerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = DateCount
        fields = '__all__'