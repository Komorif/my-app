from django.contrib import admin

from .models import Question
from .models import Product


admin.site.register(Question)

admin.site.register(Product)