from django.db import models


class Complaint(models.Model):
    url = models.URLField()
    content = models.TextField()
    is_public = models.BooleanField(default=False)
    created = models.DateTimeField(null=True, editable=False, auto_now_add=True)
    updated = models.DateTimeField(null=True, editable=False, auto_now=True)

    def __unicode__(self):
        return self.url

