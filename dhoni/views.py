from django.shortcuts import render

# Create your views here.
 

def dhoni(request):
    return render(request,'dhoni.html')

def csk(request):
    return render(request,'csk.html')
 