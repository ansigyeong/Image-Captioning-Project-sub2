from django.shortcuts import render
from .serializers import VocabularySerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Vocabulary
from datetime import datetime
from django.utils.dateformat import DateFormat

@api_view(['POST'])
def vocabulary(request):

    # 선택한 필드가 'True'인 단어 중에서 랜덤으로 30개 선정
    if 'Toeic' in request.data:
        vocas = Vocabulary.objects.filter(Toeic=True).order_by('?')[0:20]
    elif 'Opic' in request.data:
        vocas = Vocabulary.objects.filter(Opic=True).order_by('?')[0:20]
    elif 'korean_SAT' in request.data:
        vocas = Vocabulary.objects.filter(korean_SAT=True).order_by('?')[0:20]

    # 오늘 날짜를 함께 기록
    today = DateFormat(datetime.now()).format('Y-m-d')

    serializer = VocabularySerializer(vocas, many=True)

    # 날짜와 단어장을 함께 전송
    data = {
        "today": today,
        "vocabulary": serializer.data
    }

    return Response(data)