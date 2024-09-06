from django.shortcuts import render
from .models import ItemInfo
# from .forms import ItemInfoForm


# Create your views here.

def home(request):
    return render(request, 'home.html')