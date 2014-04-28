# coding=utf-8
from django import forms
from complaints.models import Complaint


class ComplainsForm(forms.ModelForm):
    def clean_content(self):
        content = self.cleaned_data['content']
        if 'spam' in content:
            raise forms.ValidationError(u"Уберите `spam` из сообщения.")

        return content

    class Meta:
        model = Complaint
        exclude = ('is_public', 'created', 'undated')
