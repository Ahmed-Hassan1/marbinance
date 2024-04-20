from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import requests
from .models import *
# Create your views here.

def SortFuture(request):

    # for x in range(len(allList)):
    #     allList[x]['priceChangePercent']=float(allList[x]['priceChangePercent'])

    symbols=Entries.objects.all().order_by('priceChange').reverse()
    context={
        "symbols":symbols
    }
    return render(request,"sorting/sortList.html",context=context)#JsonResponse(allList,safe=False)