from django import forms
from .models import Author


class AuthorForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    bio = forms.CharField(widget=forms.Textarea)
    birthday = forms.DateField()


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=200)
    content = forms.CharField(widget=forms.Textarea)
    publication_date = forms.DateField()
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    category = forms.CharField(max_length=100)
    views_count = forms.IntegerField(initial=0)
    status = forms.BooleanField(required=False)


class CommentForm(forms.Form):
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    content = forms.CharField(widget=forms.Textarea)

