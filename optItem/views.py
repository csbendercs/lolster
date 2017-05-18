from optItem.serializers import *
from rest_framework import viewsets
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import detail_route, list_route
from django.http import HttpResponse
from optItem.logic_functions import *


# Create your views here.



class ChampionViewSet(viewsets.ModelViewSet):
    queryset = Champion.objects.all()
    serializer_class = ChampionSerializer

    # must pass instance, /pk/function() --> detail route, /function() --> list route, default = get method
    @list_route()
    def getCount(self, request):
        champSet = Champion.objects.all().count()
        champSetName = Champion.objects.get(pk = 6)
        temp = champPlayed(name=champSetName, numChampionPlayed=champSet)
        temp.save()
        return HttpResponse(status=204)

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

class SummonerViewSet(viewsets.ModelViewSet):
    queryset = Summoner.objects.all()
    serializer_class = SummonerSerializer

class ChampPlayedViewSet(viewsets.ModelViewSet):
    queryset = champPlayed.objects.all()
    serializer_class = champPlayedSerializer



@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'champion': reverse('champion-list', request=request, format=format),
        'item': reverse('item-list', request=request, format=format),
        'match': reverse('match-list', request=request, format=format),
        'summoner': reverse('summoner-list', request=request, format=format),
        'champPlayed': reverse('champPlayed-list', request = request, format=format),
    })
