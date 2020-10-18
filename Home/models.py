from django.db import models

# Create your models here.

class Home(models.Model):
    name         = models.CharField(max_length=50)
    description  = models.TextField(max_length=5000) 
    image        = models.ImageField(upload_to='home/')

    def __str__(self):
        return self.name

class Meta:
        verbose_name        = 'Home'
        verbose_name_plural = 'Homes'
        #ordering            = ('name',)
        ordering            = ['-id']         