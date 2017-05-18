from optItem.models import *

class ChampAnalyser:
    def run(self):
        champset = Champion.objects.all().count()
        return champset
