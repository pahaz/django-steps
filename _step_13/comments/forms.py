# coding=utf-8
from django import forms
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.core import signing
from django.core.exceptions import ObjectDoesNotExist
from django.core.signing import BadSignature, SignatureExpired
from comments.models import Comment

__author__ = 'pahaz'

COMMENT_MAX_LENGTH = getattr(settings, 'COMMENT_MAX_LENGTH', 512)


def get_content_type_fields(from_object):
    ct = ContentType.objects.get_for_model(from_object)
    app_label, model, pk = ct.app_label, ct.model, from_object.pk
    return app_label, model, pk


class BaseSecureContentTypeFormMixin(object):
    """
    Provide `secured_content_object` field with contain content_object argument.

    Ex:
        class F(BaseSecureContentTypeFormMixin, Form):
            some_field = ...

        # create form with secured `content_object`
        f = F(content_object=some_model_instance)
        f.as_p()

        # validate form
        f = F(request.POST)
        if f.is_valid():
            f.cleaned_data['secured_content_object']  # == some_model_instance
            ...

    """
    SECURED_SALT = "BaseSecureContentTypeForm"
    SECURITY_ERROR_MESSAGE = 'security error!'
    OBJECT_DOES_NOT_EXIST_MESSAGE = 'object not exist!'

    def __init__(self, *args, **kwargs):
        """
        content_object=None
        """
        content_object = kwargs.pop('content_object', None)

        super(BaseSecureContentTypeFormMixin, self).__init__(*args, **kwargs)

        if content_object:
            d = self.generate_secured_content_object_field
            initial = d(content_object)
            self.initial['secured_content_object'] = initial

        self.fields['secured_content_object'] = \
            forms.CharField(widget=forms.HiddenInput())


    def generate_secured_content_object_field(self, for_object):
        ct = ContentType.objects.get_for_model(for_object)
        return signing.dumps(
            (ct.app_label, ct.model, for_object.pk),
            salt=self.SECURED_SALT
        )

    def validate_secured_data(self, data):
        try:
            app_label, model, pk = signing.loads(
                data,
                salt=self.SECURED_SALT)
        except (BadSignature, SignatureExpired):
            raise forms.ValidationError(self.SECURITY_ERROR_MESSAGE)
        return app_label, model, pk

    def get_content_object_from_secured_data(self, data):
        app_label, model, pk = self.validate_secured_data(data)
        try:
            ct = ContentType.objects.get_by_natural_key(app_label, model)
        except ObjectDoesNotExist:
            raise forms.ValidationError(self.OBJECT_DOES_NOT_EXIST_MESSAGE)
        return ct.get_object_for_this_type(pk=pk)

    def clean_secured_content_object(self):
        data = self.cleaned_data['secured_content_object']
        return self.get_content_object_from_secured_data(data)


class CommentForm(BaseSecureContentTypeFormMixin, forms.ModelForm):
    def save(self, commit=True):
        obj = super(CommentForm, self).save(commit=False)
        content_object = self.cleaned_data['secured_content_object']
        obj.content_object = content_object
        if commit:
            obj.save()
        return obj

    class Meta:
        model = Comment
        fields = ('message', )
