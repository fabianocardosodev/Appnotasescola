from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse

def home(request):
    user = request.user
    context = {
        'user': user
    }
    
    return render(request,"home.html")
