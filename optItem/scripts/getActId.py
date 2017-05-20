import requests
from optItem.models import *
import time

def run():
    sumList = []
    actIdList = []
    sumid = ""
    count = 0
    url_actid = "https://na1.api.riotgames.com/lol/summoner/v3/summoners/" + sumid + "?api_key=RGAPI-c393b0ed-c0d2-4968-b03e-dd4c93ea6164"

    for x in range(0, Summoner.objects.all().count()):
        sumList.append(Summoner.objects.all()[x])

    #accid skips cause of count++, fix please!!!
    for x in range(0, len(sumList)):
        sumid = sumList[x].sumid
        url_actid = "https://na1.api.riotgames.com/lol/summoner/v3/summoners/" + sumid + "?api_key=RGAPI-c393b0ed-c0d2-4968-b03e-dd4c93ea6164"
        response = requests.get(url_actid)
        data1 = response.json()
        actIdList.append(data1["accountId"])
        count = count + 1
        time.sleep(1)


    for x in range(0,len(actIdList)):
        actid = actIdList[x]
        Summoner.objects.filter(sumid = sumList[x].sumid).update(actid = actid)











