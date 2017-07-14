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
    champ1Champ = []
    champ2Champ = []
    champ3Champ = []
    champ4Champ = []
    champ5Champ = []
    champ6Champ = []
    champ7Champ = []
    champ8Champ = []
    champ9Champ = []
    champ10Champ = []

    champ1win = []
    champ2win = []
    champ3win = []
    champ4win = []
    champ5win = []
    champ6win = []
    champ7win = []
    champ8win = []
    champ9win = []
    champ10win = []
    champ1Lane = []
    champ2Lane = []
    champ3Lane = []
    champ4Lane = []
    champ5Lane = []
    champ6Lane = []
    champ7Lane = []
    champ8Lane = []
    champ9Lane = []
    champ10Lane = []


    #grab the info of the first 600 matches? or maybe 300 reduce load (:299)
    for x in range(0,len(Match.objects.all().count()[0])):
        matchid = Match.objects.all()[x].matchid
        url_match = "https://na1.api.riotgames.com/lol/match/v3/matches/" + matchid + "?api_key=RGAPI-50927e52-3d35-4204-ae2e-239355af75fa"
        response = requests.get(url_match)
        data1 = response.json()

        #game version
        gameVersionList.append(data1["gameVersion"])

        #date
        tempEpoch = data1["gameCreation"]/1000
        time1 = datetime.datetime.fromtimestamp(tempEpoch).strftime("%c")
        dateCreatedList.append(time1)

        #champlist
        for x in range(0, len(data1["participants"])):
            if(x == 0):
                champ1Champ.append(data1["participants"][x]["championId"])
            if (x == 1):
                champ2Champ.append(data1["participants"][x]["championId"])
            if (x == 2):
                champ3Champ.append(data1["participants"][x]["championId"])
            if (x == 3):
                champ4Champ.append(data1["participants"][x]["championId"])
            if (x == 4):
                champ5Champ.append(data1["participants"][x]["championId"])
            if (x == 5):
                champ6Champ.append(data1["participants"][x]["championId"])
            if (x == 6):
                champ7Champ.append(data1["participants"][x]["championId"])
            if (x == 7):
                champ8Champ.append(data1["participants"][x]["championId"])
            if (x == 8):
                champ9Champ.append(data1["participants"][x]["championId"])
            if (x == 9):
                champ10Champ.append(data1["participants"][x]["championId"])


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
        #winlist
        for x in range(0, len(data1["participants"])):

            if (x == 0):
                champ1win.append(data1["participants"][x]["stats"]["win"])
            if (x == 1):
                champ2win.append(data1["participants"][x]["stats"]["win"])
            if (x == 2):
                champ3win.append(data1["participants"][x]["stats"]["win"])
            if (x == 3):
                champ4win.append(data1["participants"][x]["stats"]["win"])
            if (x == 4):
                champ5win.append(data1["participants"][x]["stats"]["win"])
            if (x == 5):
                champ6win.append(data1["participants"][x]["stats"]["win"])
            if (x == 6):
                champ7win.append(data1["participants"][x]["stats"]["win"])
            if (x == 7):
                champ8win.append(data1["participants"][x]["stats"]["win"])
            if (x == 8):
                champ9win.append(data1["participants"][x]["stats"]["win"])
            if (x == 9):
                champ10win.append(data1["participants"][x]["stats"]["win"])

        for x in range(0, len(data1["participants"])):
            if (x == 0):
                champ1Lane.append(data1["participants"][x]["timeline"]["lane"])
            if (x == 1):
                champ2Lane.append(data1["participants"][x]["timeline"]["lane"])
            if (x == 2):
                champ3Lane.append(data1["participants"][x]["timeline"]["lane"])
            if (x == 3):
                champ4Lane.append(data1["participants"][x]["timeline"]["lane"])
            if (x == 4):
                champ5Lane.append(data1["participants"][x]["timeline"]["lane"])
            if (x == 5):
                champ6Lane.append(data1["participants"][x]["timeline"]["lane"])
            if (x == 6):
                champ7Lane.append(data1["participants"][x]["timeline"]["lane"])
            if (x == 7):
                champ8Lane.append(data1["participants"][x]["timeline"]["lane"])
            if (x == 8):
                champ9Lane.append(data1["participants"][x]["timeline"]["lane"])
            if (x == 9):
                champ10Lane.append(data1["participants"][x]["timeline"]["lane"])


    for x in range(0,len(champ1win)):
        #PLEASE CONDENSE !!!
        Match.objects.filter(matchid=(Match.objects.all()[x]).update(dateCreated = dateCreatedList[x], champ1 = champ1Champ[x], ))
        Match.objects.filter(matchid=(Match.objects.all()[x]).update(champ2=champ2Champ[x], champ3=champ3Champ[x], champ4=champ4Champ[x],
                                                                     champ5=champ5Champ[x], champ6=champ6Champ[x],
                                                                     champ7=champ7Champ[x], champ8=champ8Champ[x], champ9=champ9Champ[x],
                                                                     champ10=champ10Champ[x], champ1ItemList = itemList1[x],
                                                                     champ2ItemList=itemList2[x], champ3ItemList = itemList3[x], champ4ItemList = itemList4[x],
                                                                     champ5ItemList=itemList5[x], champ6ItemList = itemList6[x], champ7ItemList = itemList8[x],
                                                                     champ9ItemList=itemList9[x], champ10ItemList = itemList10[x], champ1win = champ1Win[x],
                                                                     champ2win=champ2Win[x], champ3win = champ3Win[x], champ4win = champ4Win[x], champ5win = champ5Win[x],
                                                                     champ6win=champ6Win[x], champ7win = champ7Win[x], champ8win = champ8Win[x], champ9win = champ9Win[x],
                                                                     champ10win=champ10Win[x], champ1Lane = champ1Lane[x], champ2Lane = champ2Lane[x], champ3Lane = champ3Lane[x],
                                                                     champ4Lane=champ4Lane[x], champ5Lane = champ5Lane[x], champ6Lane = champ6Lane[x], champ7Lane = champ7Lane[x],
                                                                     champ8Lane=champ8Lane[x], champ9Lane=champ9Lane[x], champ10Lane=champ10Lane[x],))

















