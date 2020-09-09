from django.shortcuts import render, get_object_or_404
from .serializers import NoticeSerializer, NoticeListSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Notice

@api_view(['GET'])
def notice_list(request):
    notices = Notice.objects.all()
    serializer = NoticeListSerializer(notices, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def notice_create(request):
    serializer = NoticeSerializer(date=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data)


@api_view(['GET'])
def notice_detail(request, notice_pk):
    notice = get_object_or_404(Notice, pk=notice_pk)
    serializer = NoticeSerializer(notice)
    return Response(serializer.data)