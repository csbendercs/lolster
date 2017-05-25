import requests
from optItem.models import *
import time



def run():
        matchList = []
        url_recentMatch = " "
        actid = ""
        count = 0

        #this method is really time consuming, have to iterate through every summoner in the list
        for x in range(0, Summoner.objects.all().count()):
            actid = Summoner.objects.all()[x].actid
            url_recentMatch = "https://na1.api.riotgames.com/lol/match/v3/matchlists/by-account/" + actid + "/recent?api_key=RGAPI-c393b0ed-c0d2-4968-b03e-dd4c93ea6164"
            response = requests.get(url_recentMatch)
            data1 = response.json()

            for x in range(0, len(data1["matches"])):
                if(Match.objects.filter(matchid = data1["matches"][x]["gameId"]).exists() == True or (matchList.count(data1["matches"][x]["gameId"]) >= 1)):
                    pass

                else:
                    matchList.append(data1["matches"][x]["gameId"])

            time.sleep(1.5)
            count = count + 1
            print(count)

        #should add epoch date?
        for x in range(0,len(matchList)):
            temp = Match(matchid = matchList[x],)
            temp.save()




