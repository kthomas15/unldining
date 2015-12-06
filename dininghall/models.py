from django.db import models

class Hall(models.Model):
    name = models.CharField(max_length=255) 
    name_slug=models.SlugField()
    def __unicode__(self):
        return self.name
    def get_absolute_url(self):
        return "hall/%s/" % self.name_slug
    
class Meals(models.Model):
    meal_date = models.DateField()
    hall = models.ForeignKey(Hall)
    breakfast = models.IntegerField(blank=True, null=True)
    lunch = models.IntegerField(blank=True, null=True)
    dinner = models.IntegerField(blank=True, null=True)
    late_night = models.IntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    def __unicode__(self):
        return self.hall.name
  
    
