from django.shortcuts import render
from .models import etelaat


# Create your views here.
def checkout(request):
    context = {
        'checkout': etelaat.objects.all()
    }
    return render(request, 'checkout.html', context)
