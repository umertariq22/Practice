from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Articles, Comments
import re
from django.contrib import messages


# TODO:Main Page
def main(request):
    data = Articles.objects.all()
    return render(request, 'articles/index.html', context={'data': data})


# TODO:Full Article View
def view(request, pk):

    data = Articles.objects.filter(pk=pk)
    comments = Comments.objects.filter(article_id=pk)
    return render(request, 'articles/views.html', context={'all': data, 'comment': comments})


# TODO: Delete Article
def delete(request, pk):
    data = Articles.objects.filter(pk=pk)
    data.delete()
    return redirect('articles:main')


# TODO: Edit Article
def edit(request, pk):
    if request.method == 'POST':
        pattern = re.compile(r'^[a-z|A-Z]{1}|[0-9]|\s]$')
        data = Articles.objects.filter(pk=pk)
        title = request.POST.get('title')
        if not title:
            print('Empty Title')
        elif not pattern.match(title):
            print('Not matched')
        author = request.POST.get('author')
        article = request.POST.get('article')
        published_time = timezone.now()
        save = Articles(pk=pk, title=title, author=author, article=article, published_time=published_time)
        if save.save():
            messages.success(request, 'Article edited successfully')
        else:
            messages.error(request, 'Error was not edited successfully')

    data = Articles.objects.filter(pk=pk)
    return render(request, 'articles/edit.html', context={'data': data})


# TODO: New Article
def new(request):

    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        article = request.POST.get('article')
        published_time = timezone.now()
        save = Articles(title=title, author=author, article=article, published_time=published_time)
        save.save()
    return render(request, 'articles/new.html')