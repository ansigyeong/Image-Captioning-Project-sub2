from django.shortcuts import render, get_object_or_404
from .serializers import PointSerializer, PointListSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Point, User

@api_view(['POST'])
def point_reward(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)

    serializer = PointSerializer(request)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)


@api_view(['POST'])
def point_use(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)

    serializer = PointSerializer(request)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)


@api_view(['GET'])
def point_list(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)

    points = Point.objects.filter(user=user)
    serializer = PointListSerializer(points, many=True)
    return Response(serializer.data)