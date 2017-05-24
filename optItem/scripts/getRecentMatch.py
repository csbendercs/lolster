import requests
from optItem.models import *

def run():
        matchList = []
        url_recentMatch = " "
        actid = ""

        for x in range(0, Summoner.objects.all().count()):
            actid = Summoner.objects.all()[x].actid
            url_recentMatch = "https://na1.api.riotgames.com/lol/match/v3/matchlists/by-account/" + actid + "/recent?api_key=RGAPI-c393b0ed-c0d2-4968-b03e-dd4c93ea6164"
            response = requests.get(url_recentMatch)
            data1 = response.json()

            for x in range(0, len(data1["matches"])):
                if(Match.objects.filter(matchid = data1["matches"][x]["gameId"]).exists() == True):
                    pass

                else:
                    matchList.append(data1["matches"][x]["gameId"])



        #finish the rest!!!!!
        #complete check
        #run through matchlist and store matchid numbers in DB

