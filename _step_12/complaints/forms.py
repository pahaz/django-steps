# coding=utf-8
from django import forms
from complaints.models import Complaint, Comment


class ComplainsForm(forms.ModelForm):
    def clean_content(self):
        content = self.cleaned_data['content']
        if 'spam' in content:
            raise forms.ValidationError(u"Уберите `spam` из сообщения.")

        return content

    class Meta:
        model = Complaint
        fields = ('url', 'content', 'screen')
        widgets = {
            'url': forms.TextInput(attrs={'placeholder': 'url'}),
            'content': forms.Textarea(attrs={'placeholder': 'content without spam!'})
        }


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