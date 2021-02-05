import datetime
from django.db import models


class Client(models.Model):
    """this models the client object(browser) that 
    sends a long a url"""
    client_id = models.CharField(max_length=30, unique=True)

    def __unicode__(self):
        return self.client_id


class Url(models.Model):
    created_by = models.ForeignKey(
                                    Client, 
                                    on_delete=models.SET_NULL,
                                    related_name="urls",
                                    null=True
                                    )
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

    def get_absolute_url(self):
        return self.long_url