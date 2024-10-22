import datetime

from django.db import models
from django.utils import timezone


class ModelVideo(models.Model):
    INFORMATIONAL = "informational"
    EDUCATIONAL = "educational"
    ENTERTAINING = "entertaining"

    CHOISE_GENRE = {
        (INFORMATIONAL, "informational"),
        (EDUCATIONAL, "educational"),
        (ENTERTAINING, "entertaining"),
    }

    
    image = models.ImageField(upload_to='images/', null=True)
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=50, null=True, choices=CHOISE_GENRE,default=INFORMATIONAL)
    date = models.DateField(default=timezone.now, null=True)
    month = models.CharField(max_length=8, null=True)
    description = models.CharField(max_length=130)