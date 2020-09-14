from django.contrib import admin
#관리자페이지에서 퀴즈 모델을 관리하기 위해서 
from .models import Quiz
# Register your models here.

admin.site.register(Quiz)
