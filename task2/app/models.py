from django.db import models
type_choices = [
    ("batsmen","batsmen"),
    ("bowler","bowler"),
    ("keeper","keeper")
]
# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(choices=type_choices,max_length=100)
    batting = models.IntegerField()
    bowling = models.IntegerField()
    batsmen = models.BooleanField(default=False)
    bowler = models.BooleanField(default=False)
    keeper = models.BooleanField(default=False)
    taken = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.name

