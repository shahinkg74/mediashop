from django.shortcuts import render
from.forms import tamas


# Create your views here.
def contact(request):
    form = tamas()
    return render(request, 'contact.html', {'form':form})
