from django.shortcuts import render

# Create your views here.


def virat(request):
    return render(request,'virat.html')

def rcb(request):
    return render(request,'rcb.html')