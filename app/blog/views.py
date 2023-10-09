from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .models import Author, Category, Comment, Post, PostCategory, PostTag, Tag


class PostList(ListView):
    def list(self, request):
        queryset = self.get_queryset()
        return HttpResponse(queryset.objects.first().title)

    def get_queryset(self):
        queryset = Post.objects.all()
        return queryset


class PostDetail(DetailView):
    def get(self, request, pk):
        return HttpResponse(f"Post Detail {pk}")


class PostNew(CreateView):
    def put(self, request):
        return HttpResponse("Post New")


class PostEdit(UpdateView):
    def patch(self, request, pk):
        return HttpResponse(f"Post Edit {pk}")


class PostDelete(DeleteView):
    def delete(self, request, pk):
        return HttpResponse(f"Post Delete {pk}")
