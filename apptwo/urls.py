from django.urls import path
from .views import authors_posts, add_author, author_article

urlpatterns = [
    path('author/<int:author_id>/post', authors_posts, name='authors_posts'),
    path('add_author', add_author, name='add_author'),
    path('author/articles/<int:article_id>', author_article, name='author_article'),
]
