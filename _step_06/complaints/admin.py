__author__ = 'pahaz'

from django.contrib import admin
from complaints.models import Complaint


class ComplaintAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ('url', 'content', 'is_public')
    list_display_links = ('url',)
    readonly_fields = ('created', 'updated')
    list_editable = ('is_public',)
    list_filter = ('is_public', )
    fieldsets = (
        (None, {
            'fields': ('url', 'content')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('created', 'updated')
        }),
    )



admin.site.register(Complaint, ComplaintAdmin)