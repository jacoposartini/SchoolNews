from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Article

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'object_list'

class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'article_object'
    template_name = 'article_detail.html'
