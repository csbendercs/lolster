import requests
from optItem.models import *

url_item = "https://na1.api.riotgames.com/lol/static-data/v3/items?api_key=RGAPI-17742776-9592-483a-ac52-8804556bbe1c"

response = requests.get(url_item)
itemData = response.json()

sort1 = sorted(itemData["data"].keys())

tempList1 = []
tempList2 = []
tempName = ""
tempId = ""
for x in sort1:
    if(Item.objects.filter(itemid = str(x)).exists() == True):
        pass
    else:
        try:
            tempList1.append(itemData["data"][str(x)]["name"])
            tempList2.append(itemData["data"][str(x)]["id"])
        except KeyError:
            pass

for x in range(0,len(tempList1)):
    tempName = tempList1[x]
    tempId = tempList2[x]
    blah = Item(name = tempName, itemid = tempId)
    blah.save()



