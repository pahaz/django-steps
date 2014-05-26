from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from comments.forms import CommentForm
from utils.views import LoginRequiredMixin

__author__ = 'pahaz'


class CommentCreateView(LoginRequiredMixin, CreateView):
    form_class = CommentForm
    template_name = "complaints/add_comment.html"

    def form_valid(self, form):
        self.object = form.save(False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    # success_url = self.object.get_absolute_url()