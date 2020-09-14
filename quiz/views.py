from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quiz
from .serializers import QuizSerializer
import random



# Create your views here.
@api_view(['GET'])
#함수 
def helloAPI(request):
    return Response("hello world!")

#실행되는 단계를 위해 url 을 설정해주어야 한다 
#새로운 api 추가
#주어진 개수만큼 랜덤한 퀴즈를 반환하는 api
@api_view(['GET'])
def randomQuiz(request, id):

    totalQuizs = Quiz.objects.all()
    #random 모듈 사용 import , 개수를 id 만큼
    randomQuizs = random.sample(list(totalQuizs),id)
    #many=True 해주면 다량의 데이터에 대해서도 직렬화를 제공해준다 
    serializer = QuizSerializer(randomQuizs, many=True)
    return Response(serializer.data)
