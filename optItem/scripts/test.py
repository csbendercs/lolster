import requests
from optItem.models import *
import time
import datetime

def run():
    url_match = ""

    dateCreatedList = []
    gameVersionList = []

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






    #grab the info of the first 600 matches? or maybe 300 reduce load (:299)
    for x in range(0,2):
        matchid = Match.objects.all()[x].matchid
        url_match = "https://na1.api.riotgames.com/lol/match/v3/matches/" + matchid + "?api_key=RGAPI-17742776-9592-483a-ac52-8804556bbe1c"
        response = requests.get(url_match)
        data1 = response.json()

        #game version
        gameVersionList.append(data1["gameVersion"])

        #date
        tempEpoch = data1["gameCreation"]/1000
        time1 = datetime.datetime.fromtimestamp(tempEpoch).strftime("%c")
        dateCreatedList.append(time1)

        #champlist
        for y in range(0, 10):
            if(y == 0):
                champ1Champ.append(data1["participants"][y]["championId"])
            if (y == 1):
                champ2Champ.append(data1["participants"][y]["championId"])
            if (y == 2):
                champ3Champ.append(data1["participants"][y]["championId"])
            if (y == 3):
                champ4Champ.append(data1["participants"][y]["championId"])
            if (y == 4):
                champ5Champ.append(data1["participants"][y]["championId"])
            if (y == 5):
                champ6Champ.append(data1["participants"][y]["championId"])
            if (y == 6):
                champ7Champ.append(data1["participants"][y]["championId"])
            if (y == 7):
                champ8Champ.append(data1["participants"][y]["championId"])
            if (y == 8):
                champ9Champ.append(data1["participants"][y]["championId"])
            if (y == 9):
                champ10Champ.append(data1["participants"][y]["championId"])

                # item list
                for x in range(0, len(data1["participants"])):

                    if (x == 0):
                        temp1 = []
                        temp1.append(data1["participants"][x]["stats"]["item1"])
                        temp1.append(data1["participants"][x]["stats"]["item2"])
                        temp1.append(data1["participants"][x]["stats"]["item3"])
                        temp1.append(data1["participants"][x]["stats"]["item4"])
                        temp1.append(data1["participants"][x]["stats"]["item5"])
                        temp1.append(data1["participants"][x]["stats"]["item6"])
                        itemList1.append(temp1)


                    if (x == 1):
                        temp2 = []
                        itemList2.append(data1["participants"][x]["stats"]["item1"])
                        itemList2.append(data1["participants"][x]["stats"]["item2"])
                        itemList2.append(data1["participants"][x]["stats"]["item3"])
                        itemList2.append(data1["participants"][x]["stats"]["item4"])
                        itemList2.append(data1["participants"][x]["stats"]["item5"])
                        itemList2.append(data1["participants"][x]["stats"]["item6"])
                        itemList1.append(temp2)

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



    for z in range(0,2):
        #PLEASE CONDENSE !!!
        Match.objects.filter(matchid=Match.objects.all()[z]).update(gameVersion = gameVersionList [z])
        Match.objects.filter(matchid=Match.objects.all()[z]).update(champ1 = champ1Champ[z], champ2 = champ2Champ[z], champ3 = champ3Champ[z],
                                                                    champ4=champ4Champ[z], champ5 = champ5Champ[z], champ6 = champ6Champ[z],
                                                                    champ7=champ7Champ[z], champ8 = champ8Champ[z], champ9 = champ9Champ[z],
                                                                    champ10=champ10Champ[z],)


        print(itemList1)
        print(itemList2)

        temp = Match.objects.get(matchid=Match.objects.all()[z])
        if(z == 0):
            itemT1 = Item.objects.get(itemid = itemList1[0])
            itemT2 = Item.objects.get(itemid = itemList1[1])
            itemT3 = Item.objects.get(itemid=itemList1[2])
            itemT4 = Item.objects.get(itemid=itemList1[3])
            itemT5 = Item.objects.get(itemid=itemList1[4])
            itemT6 = Item.objects.get(itemid=itemList1[5])
            print(itemT1, itemT2, itemT3, itemT4, itemT5, itemT6)
            temp.champ1ItemList.add(itemT1, itemT2, itemT3, itemT4, itemT5, itemT6)
            print("Test")
        elif(z == 1):
            itemT1 = Item.objects.get(itemid=itemList2[0])
            itemT2 = Item.objects.get(itemid=itemList2[1])
            itemT3 = Item.objects.get(itemid=itemList2[2])
            itemT4 = Item.objects.get(itemid=itemList2[3])
            itemT5 = Item.objects.get(itemid=itemList2[4])
            itemT6 = Item.objects.get(itemid=itemList2[5])
            temp.champ2ItemList.add(itemT1, itemT2, itemT3, itemT4, itemT5, itemT6)

























