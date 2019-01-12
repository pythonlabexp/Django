from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'FirstApp/index.html')

def static(request):
    return render(request,'FirstApp/ind.html')