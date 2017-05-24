from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Champion)
admin.site.register(Item)
admin.site.register(Match)
admin.site.register(champPlayed)


@admin.register(Summoner)
class SummonerAdmin(admin.ModelAdmin):
    list_display = ("name", "leaguePoints","actid")