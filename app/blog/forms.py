from django import forms

from .models import Author, Category, Comment, Post, PostCategory, PostTag, Tag


class PostNewForm(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple
    )

    tag = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Post
        fields = ["title", "content", "author", "category", "tag"]
