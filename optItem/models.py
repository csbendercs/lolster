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
    # convert epoch time to datetime instance
    dateCreated = models.DateTimeField(blank = False, null = True)


    '''
    champList = models.ManyToManyField(Champion)
    champ1ItemList = models.ManyToManyField(Item)
    champ2ItemList = models.ManyToManyField(Item)
    champ3ItemList = models.ManyToManyField(Item)
    champ4ItemList = models.ManyToManyField(Item)
    champ5ItemList = models.ManyToManyField(Item)
    champ6ItemList = models.ManyToManyField(Item)
    champ7ItemList = models.ManyToManyField(Item)
    champ8ItemList = models.ManyToManyField(Item)
    champ9ItemList = models.ManyToManyField(Item)
    champ10ItemList = models.ManyToManyField(Item)

    champ1Win = models.NullBooleanField()
    champ2Win = models.NullBooleanField()
    champ3Win = models.NullBooleanField()
    champ4Win = models.NullBooleanField()
    champ5Win = models.NullBooleanField()
    champ6Win = models.NullBooleanField()
    champ7Win = models.NullBooleanField()
    champ8Win = models.NullBooleanField()
    champ9Win = models.NullBooleanField()
    champ10Win = models.NullBooleanField()
    
    champ1lane = models.CharField(max_length = 30)
    
    '''


    def __str__(self):
        return self.matchid


class Summoner(models.Model):
    sumid = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    division = models.CharField(max_length=30)
    leaguePoints = models.IntegerField()
    #hold up to 10 for now
    recentMatches = models.ManyToManyField(Match)
    actid = models.CharField(max_length=20, blank = False, null=True)

    class Meta:
        ordering = ("-leaguePoints",)

    def __str__(self):
        return self.name

class champPlayed(models.Model):
    name = models.ForeignKey(Champion, on_delete = models.CASCADE)
    numChampionPlayed = models.IntegerField()

    def __str__(self):
        return str(self.name)







