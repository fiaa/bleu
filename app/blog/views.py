from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse_lazy
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
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        postag = PostTag.objects.filter(post=post).values_list("tag", flat=True)
        postcategory = PostCategory.objects.filter(post=post).values_list("category", flat=True)
        context['tag'] = Tag.objects.filter(id__in=postag).all()
        context['category'] = Category.objects.filter(id__in=postcategory).all()
        return context


class PostNew(CreateView):
    template_name = "blog/post_new.html"
    model = Post
    form_class = PostNewForm
    success_url = reverse_lazy("post_list")


class PostEdit(UpdateView):
    def patch(self, request, pk):
        return HttpResponse(f"Post Edit {pk}")


class PostDelete(DeleteView):
    def delete(self, request, pk):
        return HttpResponse(f"Post Delete {pk}")
