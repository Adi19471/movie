from django.db import models


# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=400)
    directory = models.CharField(max_length=380)
    cast = models.CharField(max_length=200)
    description = models.TextField(max_length=502)
    release_date = models.DateField()
    avaragerating = models.FloatField(default=0)
    image = models.URLField(default=None,null=True)

    # image = models.ImageField(upload_to='images')
    #image = models.ImageField(upload_to='images', blank=True)

    def __str__ (self):
        return self.name

    def __unicode__(self):
        return self.name