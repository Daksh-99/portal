from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=255, blank=True)
    roll = models.IntegerField()

    def __str__(self) -> str:
        return self.name


class Proj_details(models.Model):
    name = models.CharField(max_length=255)
    details = models.TextField()
    proposer = models.CharField(max_length=40)
    people = models.ManyToManyField(Person)

    def __str__(self) -> str:
        return self.name
