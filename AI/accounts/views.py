from django.shortcuts import render, get_object_or_404
from .serializers import PointSerializer, PointListSerializer, DailySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Point, User, DateCount

@api_view(['POST'])
def point_reward(request):

    user_pk = request.data['user']

    user = get_object_or_404(User, pk=user_pk)

    serializer = PointSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=user)
        return Response(serializer.data)

@api_view(['GET'])
def point_list(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)

    points = Point.objects.filter(user=user)
    
    # 해당 유저의 전체 포인트를 리스트로 정리
    user_point_list = []
    for point in points:
        if point.use_type == True:
            user_point_list.append(point.value)
        else:
            user_point_list.append(-point.value)
    
    # 합계를 구하여 user 모델의 db에 저장
    user_points = sum(user_point_list)
    user.total_point = user_points
    user.save()

    serializer = PointListSerializer(points, many=True)

    # data 라는 dict를 생성하여 total_point와 point_list를 return
    # point_list는 기존의 serializer를 활용
    data = {
        "total_points": user_points,
        "point_list": serializer.data
    }
    return Response(data)

@api_view(['POST'])
def daily(request, user_pk):
    
    # myDict에 Querydict를 dictionary로 저장
    myDict = {}
    for key in request.data:
        myDict[key] = request.data.getlist(key)
    
    # myDict의 key값을 list로 저장
    key = list(myDict.keys())
    
    # 해당 key 값을 date filter로 사용
    now = key[0]

    user = get_object_or_404(User, pk=user_pk)

    attendance = DateCount.objects.filter(user=user).filter(date=now)

    serializer = DailySerializer(attendance, many=True)
    return Response(serializer.data)