from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone  # timezone import 추가 필요
import datetime  # datetime import 추가 필요
from django.contrib import admin



class Question123(models.Model):
    question_text = models.CharField(max_length=200) #문자열 필드 생성
    pub_date = models.DateTimeField("date published") #date published값을 넣어 생성

    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def get_question_text_length(self):
        return len(self.question_text)
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_Date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


    
    
    

class Choice(models.Model): #question 은 foreignkey?
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #question 내용이 지워지면 남겨질것인지 따라갈것인지
    choice_text = models.CharField(max_length=200) 
    votes = models.IntegerField(default=0) #
    
    def __str__(self):
        return self.choice_text   
# class A:
#     pass`
from django.db import models







