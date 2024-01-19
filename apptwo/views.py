from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Author, Comments
from .forms import AuthorForm, ArticleForm, CommentForm

# Create your views here.


def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            Author.objects.create(**form.cleaned_data)
            return redirect('add_author')
    else:
        form = AuthorForm()
    return render(request, 'apptwo/add_author.html', {'form': form})


def add_post(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            Article.objects.create(**form.cleaned_data)
            return redirect('add_post')
    else:
        form = ArticleForm()
    return render(request, 'apptwo/add_article.html', {'form': form})


def author_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            Comments.objects.create(
                author=form.cleaned_data['author'],
                article=article,
                content=form.cleaned_data['content'],
            )
            return redirect('author_article', article_id=article_id)
    else:
        form = CommentForm()
    return render(request, 'apptwo/author_article.html', {'article': article, 'form': form})


def authors_posts(request, author_id):
    get_author = Author.objects.get(id=author_id)
    article = get_author.article_set.all()
    return render(request, 'apptwo/authors_posts.html', {'posts': article})
