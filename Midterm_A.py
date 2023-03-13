from django.shortcuts import render 
from django.http import HttpResponse 

def jobroles(request):
    context = {
        'Jobroles' : ['reporting', 
                      'business analyst', 
                      'statiscian', 
                      'data scitist', 
                      'data engineer/data architect', 
                      'machine learning engineer', 
                      'big data engineer']
        }

    
    return render(request, "midterma.html" ,context)
