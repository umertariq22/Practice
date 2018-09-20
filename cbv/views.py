from django.views.generic import TemplateView,DeleteView,ListView,UpdateView,View,CreateView,DetailView
from . import models
from django.urls import reverse_lazy


class MainPageView(TemplateView):
    template_name = 'cbv/index.html'


class CreateArticle(CreateView):
    fields = ('title','text')
    model = models.Article


class DetailViewArticle(DetailView):
    context_object_name = 'article_data'
    model = models.Article
    template_name = 'cbv/detailview.html'

class UpdateViewArticles(UpdateView):
    model = models.Article
    fields = ('title', 'text')
    success_url = reverse_lazy('cbv:index')


class DeleteViewArticle(DeleteView):
    model = models.Article
    success_url = reverse_lazy('cbv:index')