from django.shortcuts import render
from .models import kart


# Create your views here.

def cart(request):
    all = kart.objects.all()
    return render(request, 'cart.html', {'all':all})
