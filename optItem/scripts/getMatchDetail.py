import requests
from optItem.models import *
import time

def run():
    url_match = ""

    dateCreatedList = []
    gameVersionList = []



    #grab the info of the first 600 matches?
    for x in range(0,len(Match.objects.all().count()[:599])):
        matchid = Match.objects.all()[x].matchid
        url_match = "https://na1.api.riotgames.com/lol/match/v3/matches/" + matchid + "?api_key=RGAPI-c393b0ed-c0d2-4968-b03e-dd4c93ea6164"
        response = requests.get(url_match)
        data1 = response.json()

