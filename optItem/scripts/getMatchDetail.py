import requests
from optItem.models import *
import time
import datetime

def run():
    url_match = ""

    dateCreatedList = []
    gameVersionList = []
    itemList1 = []
    itemList2 = []
    itemList3 = []
    itemList4 = []
    itemList5 = []
    itemList6 = []
    itemList7 = []
    itemList8 = []
    itemList9 = []
    itemList10 = []

    #grab the info of the first 600 matches?
    for x in range(0,len(Match.objects.all().count()[:299])):
        matchid = Match.objects.all()[x].matchid
        url_match = "https://na1.api.riotgames.com/lol/match/v3/matches/" + matchid + "?api_key=RGAPI-c393b0ed-c0d2-4968-b03e-dd4c93ea6164"
        response = requests.get(url_match)
        data1 = response.json()

        #game version
        gameVersionList.append(data1["gameVersion"])

        #date
        tempEpoch = data1["gameCreation"]/1000
        time1 = datetime.datetime.fromtimestamp(tempEpoch).strftime("%c")
        dateCreatedList.append(time1)

        #item list
        for x in range(0, len(data1["participants"])):

            if (x == 0):
                itemList1.append(data1["participants"][x]["stats"]["item1"])
                itemList1.append(data1["participants"][x]["stats"]["item2"])
                itemList1.append(data1["participants"][x]["stats"]["item3"])
                itemList1.append(data1["participants"][x]["stats"]["item4"])
                itemList1.append(data1["participants"][x]["stats"]["item5"])
                itemList1.append(data1["participants"][x]["stats"]["item6"])

            if (x == 1):
                itemList2.append(data1["participants"][x]["stats"]["item1"])
                itemList2.append(data1["participants"][x]["stats"]["item2"])
                itemList2.append(data1["participants"][x]["stats"]["item3"])
                itemList2.append(data1["participants"][x]["stats"]["item4"])
                itemList2.append(data1["participants"][x]["stats"]["item5"])
                itemList2.append(data1["participants"][x]["stats"]["item6"])

            if (x == 2):
                itemList3.append(data1["participants"][x]["stats"]["item1"])
                itemList3.append(data1["participants"][x]["stats"]["item2"])
                itemList3.append(data1["participants"][x]["stats"]["item3"])
                itemList3.append(data1["participants"][x]["stats"]["item4"])
                itemList3.append(data1["participants"][x]["stats"]["item5"])
                itemList3.append(data1["participants"][x]["stats"]["item6"])

            if (x == 3):
                itemList4.append(data1["participants"][x]["stats"]["item1"])
                itemList4.append(data1["participants"][x]["stats"]["item2"])
                itemList4.append(data1["participants"][x]["stats"]["item3"])
                itemList4.append(data1["participants"][x]["stats"]["item4"])
                itemList4.append(data1["participants"][x]["stats"]["item5"])
                itemList4.append(data1["participants"][x]["stats"]["item6"])

            if (x == 4):
                itemList5.append(data1["participants"][x]["stats"]["item1"])
                itemList5.append(data1["participants"][x]["stats"]["item2"])
                itemList5.append(data1["participants"][x]["stats"]["item3"])
                itemList5.append(data1["participants"][x]["stats"]["item4"])
                itemList5.append(data1["participants"][x]["stats"]["item5"])
                itemList5.append(data1["participants"][x]["stats"]["item6"])

            if (x == 5):
                itemList6.append(data1["participants"][x]["stats"]["item1"])
                itemList6.append(data1["participants"][x]["stats"]["item2"])
                itemList6.append(data1["participants"][x]["stats"]["item3"])
                itemList6.append(data1["participants"][x]["stats"]["item4"])
                itemList6.append(data1["participants"][x]["stats"]["item5"])
                itemList6.append(data1["participants"][x]["stats"]["item6"])

            if (x == 6):
                itemList7.append(data1["participants"][x]["stats"]["item1"])
                itemList7.append(data1["participants"][x]["stats"]["item2"])
                itemList7.append(data1["participants"][x]["stats"]["item3"])
                itemList7.append(data1["participants"][x]["stats"]["item4"])
                itemList7.append(data1["participants"][x]["stats"]["item5"])
                itemList7.append(data1["participants"][x]["stats"]["item6"])

            if (x == 7):
                itemList8.append(data1["participants"][x]["stats"]["item1"])
                itemList8.append(data1["participants"][x]["stats"]["item2"])
                itemList8.append(data1["participants"][x]["stats"]["item3"])
                itemList8.append(data1["participants"][x]["stats"]["item4"])
                itemList8.append(data1["participants"][x]["stats"]["item5"])
                itemList8.append(data1["participants"][x]["stats"]["item6"])

            if (x == 8):
                itemList9.append(data1["participants"][x]["stats"]["item1"])
                itemList9.append(data1["participants"][x]["stats"]["item2"])
                itemList9.append(data1["participants"][x]["stats"]["item3"])
                itemList9.append(data1["participants"][x]["stats"]["item4"])
                itemList9.append(data1["participants"][x]["stats"]["item5"])
                itemList9.append(data1["participants"][x]["stats"]["item6"])

            if (x == 9):
                itemList10.append(data1["participants"][x]["stats"]["item1"])
                itemList10.append(data1["participants"][x]["stats"]["item2"])
                itemList10.append(data1["participants"][x]["stats"]["item3"])
                itemList10.append(data1["participants"][x]["stats"]["item4"])
                itemList10.append(data1["participants"][x]["stats"]["item5"])
                itemList10.append(data1["participants"][x]["stats"]["item6"])














