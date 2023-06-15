from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    date ={
        'title': 'Main page',
        'values': ['Some','Hello','123'],
        'obj': {'car': 'bmw',
                'age': 18,
                'hobby': 'football'}
    }

    return render(request,'main/index.html', date)

def about(request):
    return render(request,'main/about.html')