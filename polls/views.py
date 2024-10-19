from django.http import HttpResponse


# Для БД
from django.shortcuts import render
from polls.models import Product


def index(request):
    product = Product.objects.all()

    context = {
        "pr": product
    }
    return render(request, 'web/index.html', context)

#def index(request):
#    questions = Question.objects.all()
#   return render(request, 'web/index.html', {'questions': questions})


def polls(request):
    return HttpResponse("Hello World. This is polls!")