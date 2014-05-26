from django import template
from django.contrib.contenttypes.models import ContentType
from comments.forms import CommentForm
from comments.models import Comment

__author__ = 'pahaz'

register = template.Library()


# {% get_comment_list for [object] as [varname]  %}
# {% get_comment_form for [object] as [varname] %}


@register.assignment_tag
def get_comment_form(object):
    return CommentForm(content_object=object)


@register.assignment_tag
def get_comment_list(object):
    ct = ContentType.objects.get_for_model(object)
    return Comment.objects.filter(content_type=ct, object_id=object.pk)