import datetime

from django.db import models
from django.utils import timezone


class ModelVideo(models.Model):
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=130)