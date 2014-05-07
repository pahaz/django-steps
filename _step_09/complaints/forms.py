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
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content':forms.TextInput(attrs={'placeholder': 'message'}),
        }