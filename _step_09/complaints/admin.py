from complaints.forms import CommentForm
from complaints.models import Comment

__author__ = 'pahaz'

from django.contrib import admin
from complaints.models import Complaint


class CommentsInline(admin.TabularInline):
    model = Comment
    extra = 1
    form = CommentForm


class ComplaintAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ('url', 'content', 'is_public', 'screen')
    list_display_links = ('url',)
    readonly_fields = ('created', 'updated')
    list_editable = ('is_public',)
    list_filter = ('is_public', )
    fieldsets = (
        (None, {
            'fields': ('url', 'content', 'screen')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('created', 'updated')
        }),
    )
    inlines = [
        CommentsInline,
    ]


admin.site.register(Complaint, ComplaintAdmin)