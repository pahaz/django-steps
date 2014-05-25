from django.views.generic import CreateView
from comments.forms import CommentForm
from utils.views import LoginRequiredMixin

__author__ = 'pahaz'


class ComplaintCommentCreateView(LoginRequiredMixin, CreateView):
    form_class = CommentForm
    template_name = "complaints/add_comment.html"
    # success_url = self.object.get_absolute_url()