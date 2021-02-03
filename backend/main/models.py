import datetime
from django.db import models


class Url(models.Model):
    long_url = models.URLField(max_length=500)
    shortcode = models.CharField(max_length=30, unique=True)
    hits = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    last_accessed = models.DateTimeField(null=True)

    def __unicode__(self):
        return self.shortcode

    def visited(self):
        self.hits += 1
        self.last_accessed = datetime.datetime.now()
        self.save()