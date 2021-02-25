from django.shortcuts import render
from .models import Merchant

# Create your views here.
def index(request):
    merchants=Merchant.objects.all()
    context={
        'merchants':merchants
        #'rambilas':'bimalpaan masala'
    }
    return render(request,'merchants/merchantList.html',context)


def profile(request,merchant):
    merchantProfile=Merchant.objects.get(id=merchant)
    context={
        # 'pageRoute:merchant',
        'merchant':merchantProfile
    }
    return render(request,'merchants/merchantProfile.html',context)

###
def search(request):
    merchantName=request.POST['merchantName']
    merchants=Merchant.objects.filter(name_contains=merchantName)
    context={
        'keyword':merchantName,
        'merchants':merch
    
    }
    return render(request, 'merchants/merchantSearch.html',context)


def search(request):
    listName=request.POST['listName']
    lists=List.objects.filter(name_contains=listName)
    context={
        'keyword':listName,
        'lists':lizt
    
    }
    return render(request, 'lists/listSearch.html',context)


