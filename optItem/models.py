from django.db import models

RANK_CHOICES = ["BRONZE", "SILVER", "GOLD", "PLAT", "DIAMOND", "MASTER", "CHALLENGER"]


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    itemid = models.CharField(max_length=20)

    class Meta:
        ordering = ("itemid",)

    def __str__(self):
        return self.name


class Champion(models.Model):
    name = models.CharField(max_length=100)
    champid = models.CharField(max_length=20)
    itemList = models.ManyToManyField(Item)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Match(models.Model):
    matchid = models.CharField(max_length=20)

    def __str__(self):
        return self.matchid


class Summoner(models.Model):
    sumid = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    division = models.CharField(max_length=30)
    rankPos = models.IntegerField()
    #hold up to 10 for now
    recentMatches = models.ManyToManyField(Match)
    actid = models.CharField(max_length=20, blank = False, null=True)

    class Meta:
        ordering = ("-rankPos",)

    def __str__(self):
        return self.name

class champPlayed(models.Model):
    name = models.ForeignKey(Champion, on_delete = models.CASCADE)
    numChampionPlayed = models.IntegerField()

    def __str__(self):
        return str(self.name)







