from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, resolve_url

complaints = [
    {
        'url': "http://ya.ru/",
        'content': "I can't find my site!",
    },
    {
        'url': "http://google.ru/",
        'content': "I can't find my site too!",
    },
]


def index(request):
    global complaints
    return render(request, 'complaints.html', {'complaints': complaints})


def post(request):
    global complaints
    if request.method == 'POST':
        url = request.POST.get('url')
        content = request.POST.get('content')

        complaints.append({
            'url': url,
            'content': content,
        })

    return redirect('complaints_index')