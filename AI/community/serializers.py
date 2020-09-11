from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import Notice, Suggestion, Comment

class NoticeListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Notice
        fields = ('id', 'title','content','user',)


class NoticeSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = Notice
        fields = '__all__'
        read_only_fields = ('id', 'user', 'created_at',)


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = Comment
        fields = '__all__'


class SuggestionListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Suggestion
        fields = '__all__'


class SuggestionSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Suggestion
        fields = '__all__'


