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
        fields = ("matchid",)

class SummonerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Summoner
        fields = ("url", "sumid", "name", "division", "rankPos", "recentMatches")

class champPlayedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = champPlayed
        fields = ("name", "numChampionPlayed")
