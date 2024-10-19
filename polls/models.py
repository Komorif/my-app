import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Product(models.Model):
    MOBILE = "mobile"
    NOTEBOOK = "notebook"
    PC = "pc"
    ACC = 'accessories'

    CHOICE_GROUP = {
        (MOBILE, 'mobile'),
        (NOTEBOOK, 'notebook'),
        (PC, "pc"),
        (ACC, 'accessories'),
    }


    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    availability = models.BooleanField()

    group = models.CharField(max_length=20, choices=CHOICE_GROUP, default=MOBILE)
    def _＿str＿_(self):
        return f'{self.name}'