from django.db import models


# Create your models here.
class DjangoClasses(models.Model):#setting up DjangoClasses and it's attributes
    title = models.CharField(max_length=60, default="", blank=True, null=False)
    courseNumber = models.IntegerField(blank=False, null=False)
    instructor = models.CharField(max_length=25, default="", blank=True, null=False)
    duration = models.FloatField(max_length=6, blank=True, null=False)

    objects = models.Manager()#assign the manager a variable

    def __str__(self):
        return self.instructor #use the instructor of the class to identify.
