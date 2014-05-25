from django import template

__author__ = 'pahaz'

register = template.Library()


@register.assignment_tag
def complaint_comment_form_for(complaint):
    return CommentForm(initial={'complaint': complaint})