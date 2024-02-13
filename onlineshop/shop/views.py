from django.shortcuts import render
from .models import kharid


# Create your views here.
def shop(request):
    context = {
        'ajnas': kharid.objects.all()
    }
    return render(request, 'shop.html', context)
