from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import Q
from datetime import datetime


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

    def is_published(self):
        now = datetime.now()
        return self.is_public and (self.publish_date is None or self.publish_date < now) \
            and (self.expiry_date is None or self.expiry_date > now)

    class Meta:
        abstract = True


class Timable(models.Model):
    created = models.DateTimeField(null=True, editable=False, auto_now_add=True)
    updated = models.DateTimeField(null=True, editable=False, auto_now=True)

    class Meta:
        abstract = True


class Complaint(Displayable, Timable):
    url = models.URLField()
    content = models.TextField()
    screen = models.ImageField(upload_to="complaints_img", blank=True, null=True)

    def __unicode__(self):
        return self.url

    def get_absolute_url(self):
        return reverse('complaints_detail', args=(self.pk,))
