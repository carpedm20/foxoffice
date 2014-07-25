from django.db import models

# Create your models here.
class Movie(models.model):
    date = models.DateField()
    rank = models.IntegerField()
    
    title = models.CharField(max_length=100)
    url = models.UrlField()

    def __unicode__(self):
        return "[%s] %s. %s" % (self.date.strftime("%Y%m%d"),
                                self.rank
                                self.title)
