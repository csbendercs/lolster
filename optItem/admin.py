from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Champion)
admin.site.register(Item)
admin.site.register(Match)
admin.site.register(Summoner)
admin.site.register(champPlayed)