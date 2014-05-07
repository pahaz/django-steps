# coding=utf-8
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, resolve_url
from complaints.models import Complaint


def index(request):
    errors = []
    if request.method == "POST":
        url = request.POST.get('url')
        content = request.POST.get('content')

        if not url:
            errors.append(u"Заполните `url`.")

        if not content:
            errors.append(u'Заполни `content`.')

        if "spam" in content:
            errors.append(u'Уберите `spam` из сообщения.')

        if not errors:
            Complaint.objects.create(url=url, content=content)
    else:
        url, content = "", ""

    complaints = Complaint.objects.all()
    return render(request, 'complaints.html',
                  {
                      'complaints': complaints,
                      'errors': errors,
                      'url': url,
                      'content': content,
                  })