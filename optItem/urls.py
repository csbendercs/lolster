# use chrome://net-internals --> arrow --> tool --> clear cache if redirect error
from django.conf.urls import url, include
from optItem import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'champion', views.ChampionViewSet)
router.register(r'item', views.ItemViewSet)
router.register(r'match', views.MatchViewSet)
router.register(r'summoner', views.SummonerViewSet)
router.register(r'champPlayed', views.ChampPlayedViewSet)

urlpatterns = [
	url(r'^', include(router.urls)),
]