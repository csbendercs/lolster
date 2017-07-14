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
    gameVersion = models.CharField(max_length=50, default = "")



    champ1 = models.CharField(max_length=20, default= "")
    champ2 = models.CharField(max_length=20, default= "")
    champ3 = models.CharField(max_length=20, default= "")
    champ4 = models.CharField(max_length=20, default= "")
    champ5 = models.CharField(max_length=20, default= "")
    champ6 = models.CharField(max_length=20, default= "")
    champ7 = models.CharField(max_length=20, default= "")
    champ8 = models.CharField(max_length=20, default= "")
    champ9 = models.CharField(max_length=20, default= "")
    champ10 = models.CharField(max_length=20, default= "")


    champ1ItemList = models.ManyToManyField(Item, related_name = "champ1ItemList")
    champ2ItemList = models.ManyToManyField(Item, related_name = "champ2ItemList")
    champ3ItemList = models.ManyToManyField(Item, related_name = "champ3ItemList")
    champ4ItemList = models.ManyToManyField(Item, related_name = "champ4ItemList")
    champ5ItemList = models.ManyToManyField(Item, related_name = "champ5ItemList")
    champ6ItemList = models.ManyToManyField(Item, related_name = "champ6ItemList")
    champ7ItemList = models.ManyToManyField(Item, related_name = "champ7ItemList")
    champ8ItemList = models.ManyToManyField(Item, related_name = "champ8ItemList")
    champ9ItemList = models.ManyToManyField(Item, related_name = "champ9ItemList")
    champ10ItemList = models.ManyToManyField(Item , related_name = "champ10ItemList")

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
    
    champ1lane = models.CharField(max_length=30, default= "")
    champ2lane = models.CharField(max_length=30, default= "")
    champ3lane = models.CharField(max_length=30, default= "")
    champ4lane = models.CharField(max_length=30, default= "")
    champ5lane = models.CharField(max_length=30, default= "")
    champ6lane = models.CharField(max_length=30, default= "")
    champ7lane = models.CharField(max_length=30, default= "")
    champ8lane = models.CharField(max_length=30, default= "")
    champ9lane = models.CharField(max_length=30, default= "")
    champ10lane = models.CharField(max_length=30, default= "")



    class meta:
        ordering = ("dateCreated")


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







