from django import forms

from .models import Category, Post, Tag


class PostNewForm(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        required=False,
        blank=True,
        widget=forms.SelectMultiple,
    )

    tag = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        blank=True,
        widget=forms.SelectMultiple,
    )

    class Meta:
        model = Post
        fields = ["title", "content", "author", "category", "tag"]
