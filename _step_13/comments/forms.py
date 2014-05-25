# coding=utf-8
from django import forms
from comments.models import Comment

__author__ = 'pahaz'


class CommentForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super(CommentForm, self).clean()

        complaint = cleaned_data.get('complaint')
        if not complaint or (complaint and not complaint.is_published()):
            raise forms.ValidationError(u"Вы пытаетесь написать комментарий к неопубликованной жалобе.")

        return cleaned_data

    class Meta:
        model = Comment
        fields = ('content', 'complaint')
        widgets = {
            'content': forms.TextInput(attrs={'placeholder': 'message'}),
            'complaint': forms.HiddenInput(),
        }
