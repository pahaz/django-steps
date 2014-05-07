__author__ = 'pahaz'

from django.contrib import admin
from complaints.models import Complaint

admin.site.register(Complaint)