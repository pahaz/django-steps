from django.db import models


class Complaint(models.Model):
    url = models.URLField()
    content = models.TextField()
    is_public = models.BooleanField(default=False)

    def __unicode__(self):
        return self.url
