from django.shortcuts import render
from .models import ItemInfo
from .forms import ItemInfoForm


# Create your views here.

def home(request):
    form = ItemInfoForm()
    if request.method=="POST":
        form = ItemInfoForm(request.POST,request.FILES)
        if form.is_vaild():
            form.save()
    
    data = ItemInfo.objects.all()
    return render(request,"home.html",{'form':form,'data':data})


def cart(request):
    print(request.POST)
    
    
def addtocart(request):
    print(request.POST)