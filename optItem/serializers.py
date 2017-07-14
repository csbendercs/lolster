from rest_framework import serializers
from optItem.models import *
from django.contrib.auth.models import User

class ChampionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:

        model = Champion
        fields = ("url","name", "champid", "itemList")


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ("url", "name", "itemid")

class MatchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Match
        fields = ("matchid", "gameVersion", "dateCreated", "champ1", "champ2", "champ3", "champ4", "champ5", "champ6",
                  "champ7", "champ8", "champ9", "champ10", "champ1ItemList", "champ2ItemList", "champ3ItemList", "champ4ItemList",
                  "champ5ItemList", "champ6ItemList", "champ7ItemList", "champ8ItemList", "champ9ItemList", "champ10ItemList")

class SummonerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Summoner
        fields = ("url", "sumid","actid","name", "division", "leaguePoints", "recentMatches")

class champPlayedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = champPlayed
        fields = ("name", "numChampionPlayed")
