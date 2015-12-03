from django.db import models

class Meals(models.Model):
    name = models.Charfield(max_length=255)
    name_slug = models.SlugField()
    site_id = models.CharField(max_length=3)
    def __unicode__(self):
        return self.name
    
class Hall(models.Model):
    name = models.Charfield(max_length=255) 
    name_slug=models.SlugField()
    site_id = models.CharField(max_length=3)
     def __unicode__(self):
        return self.name
    
class MealCount(models.Model):
    meal = models.ForeignKey(Meals)
    hall = models.ForeignKey(Hall)
        

  
    
