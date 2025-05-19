from django.shortcuts import render

def home(request):
    
    context = {
        'messaggio': 'Benvenuto nella homepage!',
        'area':'1000',
        'perimetro':'100'
    }

    return render(request, 'home.html', context)
