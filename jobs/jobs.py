from sorting.models import *
import requests

def job_1():
    base="https://fapi.binance.com"
    url="/fapi/v1/ticker/24hr"


    result=requests.get(base+url)

    allList=result.json()

    allList = sorted(allList, key=lambda k:float(k['priceChangePercent']),reverse=True)
    #print(allList[0])
    for x in range(len(allList)):
        if allList[x]['symbol']=='DGBUSDT':
            allList.pop(x)
            break
    
    for x in range(len(allList)):
        symbol,created=Entries.objects.get_or_create(name=allList[x]['symbol'])
        
        if created:
            symbol.currentRank=x+1
            symbol.priceChange=float(allList[x]['priceChangePercent'])
            symbol.price=float(allList[x]['lastPrice'])
            symbol.save()
        else:
            if (x+1)!=symbol.currentRank:
                symbol.previousRrank=symbol.currentRank
                symbol.currentRank=x+1
                symbol.priceChange=float(allList[x]['priceChangePercent'])
                symbol.price=float(allList[x]['lastPrice'])
                symbol.save()
            else:
                symbol.priceChange=float(allList[x]['priceChangePercent'])
                symbol.price=float(allList[x]['lastPrice'])
                symbol.save()

        
