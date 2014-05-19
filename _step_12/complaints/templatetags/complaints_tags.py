import datetime
from django import template
from complaints.forms import CommentForm
from complaints.models import Complaint

__author__ = 'pahaz'

register = template.Library()


@register.filter
def replace(value, a, b):
    return value.replace(a, b)


@register.simple_tag(takes_context=True)
def current_time(context, format_string):
    """
    Example use:

        {% current_time "%Y-%M-%d %I:%M %p" %}
    """
    return datetime.datetime.now().strftime(format_string)


# The first argument *must* be called "context" here.
# Register the custom tag as an inclusion tag with takes_context=True.
@register.inclusion_tag('complaints/tag_url_box.html', takes_context=True)
def complaints_urls(context, count_urls):
    """
    Use example:

        <div class="example-2">
            {% complaints_urls 3 %}
        </div>
    """
    return {
        'complaints': Complaint.objects.all()[:count_urls],
    }


@register.assignment_tag(takes_context=True)
def complaints(context, count_complaints):
    """
    Use example:

        <div class="example-1">
            {% complaints 2 as foo %}
            {% for x in foo %}
                {{ x.url }}
                {% if not forloop.last %} | {% endif %}
            {% endfor %}
        </div>
    """
    return Complaint.objects.all()[:count_complaints]


@register.assignment_tag
def complaint_comment_form_for(complaint):
    return CommentForm(initial={'complaint': complaint})