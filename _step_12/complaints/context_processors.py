from complaints.models import Complaint

__author__ = 'stribog'


def complaints(request):
    return {
        'complaints' : Complaint.objects.all(),
    }