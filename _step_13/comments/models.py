from django.contrib.contenttypes.generic import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth import get_user_model

__author__ = 'pahaz'


class Comment(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    message = models.TextField("Comment")

    user = models.ForeignKey(get_user_model())
    created = models.DateTimeField(null=True, editable=False, auto_now_add=True)
    updated = models.DateTimeField(null=True, editable=False, auto_now=True)

    def __unicode__(self):
        return self.comment
