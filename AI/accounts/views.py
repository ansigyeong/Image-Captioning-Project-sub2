from django.shortcuts import render, get_object_or_404
from .serializers import PointSerializer, PointListSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Point, User

@api_view(['POST'])
def point_reward(request):

    user_pk = request.data['user']

    user = get_object_or_404(User, pk=user_pk)

    serializer = PointSerializer(data=request.data)
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
    user_point_list = []
    for point in points:
        user_point_list.append(point.value)
    user_points = sum(user_point_list)
    user.total_point = user_points
    user.save()
    serializer = PointListSerializer(points, many=True)
    data = {
        "total_points": user_points,
        "point_list": serializer.data
    }
    return Response(data)