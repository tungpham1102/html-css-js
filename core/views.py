from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def code_and_create(request):
    return render(request, 'code_and_create.html')
