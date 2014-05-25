# coding=utf-8
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, resolve_url, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, View
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.list import MultipleObjectMixin
from complaints.forms import ComplainsForm, CommentForm
from complaints.models import Complaint
from utils.views import LoginRequiredMixin


def index(request):
    if request.method == "POST":
        form = ComplainsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('complaints_index')

    else:
        form = ComplainsForm()

    complaints = Complaint.objects.published()
    return render(request, 'complaints/index.html',
                  {
                      'complaints': complaints,
                      'form': form,
                  })


def detail(request, pk):
    complaints = Complaint.objects.published()
    complaint = get_object_or_404(complaints, pk=pk)
    return render(request, 'complaints/detail.html', {'item': complaint})


#########################
#                       #
#   Class Based Views   #
#                       #
#########################


class ComplaintDetailView(DetailView):
    context_object_name = 'item'
    template_name = 'complaints/detail.html'
    queryset = Complaint.objects.published()


class ComplaintIndexView(MultipleObjectMixin, CreateView):
    """
        Simple example:

            class SimpleComplaintIndexView(ListView):
                context_object_name = 'complaints'
                template_name = 'complaints/index.html'
                queryset = Complaint.objects.published()
    """
    form_class = ComplainsForm
    success_url = reverse_lazy('complaints_index')
    template_name = 'complaints/index.html'

    context_object_name = 'complaints'
    queryset = Complaint.objects.published()
    paginate_by = 3

    def get_context_data(self, **kwargs):
        # self.object_list - need for MultipleObjectMixin
        kwargs['object_list'] = self.object_list = self.get_queryset()
        context = super(ComplaintIndexView, self).get_context_data(**kwargs)
        return context
