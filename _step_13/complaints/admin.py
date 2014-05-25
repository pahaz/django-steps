# from complaints.forms import CommentForm
# from complaints.models import Comment

__author__ = 'pahaz'

from django.conf import settings
from django.contrib import admin
from complaints.models import Complaint


# class CommentsInline(admin.TabularInline):
#     model = Comment
#     extra = 1
#     form = CommentForm


class ComplaintAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ('url', 'content', 'is_public', 'get_preview_screen_img',)  # 'get_count_comments')
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

    # inlines = [
    #     CommentsInline,
    # ]

    # def get_count_comments(self, complaint):
    #     return complaint.comment_set.all().count()
    # get_count_comments.short_description = u"Count comments"

    def get_preview_screen_img(self, complaint):
        if complaint.screen:
            return "<img src='{1}{0}' height=50>".format(complaint.screen, settings.MEDIA_URL)
        return "Noooop!"
    get_preview_screen_img.short_description = u"Screen"
    get_preview_screen_img.allow_tags = True

admin.site.register(Complaint, ComplaintAdmin)