from django.db import models


class Complaint(models.Model):
    url = models.URLField()
    content = models.TextField()

    def __unicode__(self):
        return self.url
