#큐즈앱에 대한 url을 관리해주는 것이고
#myapi 는 전체 프로젝트에 대한 url을 관리합니다.
#quiz앱에 있는 url을 먼저 설정하고 이것을 myapi url에 연결시킨다.

from django.urls import path, include
from .views import helloAPI, randomQuiz

urlpatterns = [
   path("hello/",helloAPI),
   path("<int:id>/",randomQuiz),
]
 