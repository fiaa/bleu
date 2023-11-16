from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .models import Author, Category, Comment, Post, PostCategory, PostTag, Tag
from .forms import PostNewForm


class PostList(ListView):
    template_name = "blog/post_list.html"
    context_object_name = "posts_list"
    model = Post


class PostDetail(DetailView):
    template_name = "blog/post_detail.html"
    context_object_name = "post_detail"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # post = get_object_or_404(Post, pk=self.kwargs['pk'])
        post = self.object
        postag = PostTag.objects.filter(post=post)
        postcategory = PostCategory.objects.filter(post=post)

        context['tag'] = [tag.tag for tag in postag]
        context['category'] = [category.category for category in postcategory]

        return context


class PostNew(CreateView):
    template_name = "blog/post_new.html"
    model = Post
    form_class = PostNewForm

    def get_success_url(self):
        return reverse("post_detail", kwargs={"pk": self.object.pk})

class PostEdit(UpdateView):
    template_name = "blog/post_edit.html"
    model = Post
    form_class = PostNewForm

    def get_success_url(self):
        return reverse("post_detail", kwargs={"pk": self.object.pk})

class PostDelete(DeleteView):
    template_name = "blog/post_delete.html"
    model = Post

    def get_success_url(self):
        return reverse("post_list")
