from django.db import models
from django.db.models import Q
from datetime import datetime
from django import forms


class PublishedManager(models.Manager):
    def published(self, for_user=None):
        if for_user is not None and for_user.is_staff:
            return self.all()
        return self.filter(
            Q(publish_date__lte=datetime.now()) | Q(publish_date__isnull=True),
            Q(expiry_date__gte=datetime.now()) | Q(expiry_date__isnull=True),
            is_public=True)


class Displayable(models.Model):
    publish_date = models.DateTimeField(
        "Published from",
        help_text="With Published chosen, won't be shown until this time",
        blank=True, null=True)
    expiry_date = models.DateTimeField(
        "Expires on",
        help_text="With Published chosen, won't be shown after this time",
        blank=True, null=True)
    is_public = models.BooleanField(default=False)

    objects = PublishedManager()

    class Meta:
        abstract = True


class Contentable(models.Model):
    content = models.TextField()

    class Meta:
        abstract = True


class Timable(models.Model):
    created = models.DateTimeField(null=True, editable=False, auto_now_add=True)
    updated = models.DateTimeField(null=True, editable=False, auto_now=True)

    class Meta:
        abstract = True


class Complaint(Displayable, Contentable, Timable):
    url = models.URLField()
    screen = models.ImageField(upload_to="complaints_img", blank=True, null=True)

    def __unicode__(self):
        return self.url


class Comment(Timable):
    complaint = models.ForeignKey(Complaint)
    content = models.TextField()
