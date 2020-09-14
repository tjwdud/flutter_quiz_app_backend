from django.db import models

# Create your models here.

#클래스를 선언
class Quiz(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    answer = models.IntegerField()

#시리얼라이저 장고 모델 데이터를 JSON 타입으로 바꿔주는(직렬화)코드
#모델데이터를 api 통신이 가능하도록 JSON으로 바꿔주는 빵틀
