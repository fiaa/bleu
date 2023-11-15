from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .models import Author, Category, Comment, Post, PostCategory, PostTag, Tag


class PostList(ListView):
    template_name = "blog/post_list.html"
    context_object_name = "posts_list"
    model = Post


class PostDetail(DetailView):
    template_name = "blog/post_detail.html"
    context_object_name = "post_detail"
    model = Post


class PostNew(CreateView):
    def put(self, request):
        return HttpResponse("Post New")


class PostEdit(UpdateView):
    def patch(self, request, pk):
        return HttpResponse(f"Post Edit {pk}")


class PostDelete(DeleteView):
    def delete(self, request, pk):
        return HttpResponse(f"Post Delete {pk}")
