# coding=utf-8
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, resolve_url
from complaints.forms import ComplainsForm
from complaints.models import Complaint


def index(request):
    if request.method == "POST":
        form = ComplainsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('complaints_index')

    else:
        form = ComplainsForm()

    complaints = Complaint.objects.all()
    return render(request, 'complaints.html',
                  {
                      'complaints': complaints,
                      'form': form,
                  })