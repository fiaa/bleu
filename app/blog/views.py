from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .models import Author, Category, Comment, Post, PostCategory, PostTag, Tag


class PostList(ListView):
    template_name = "blog/post_list.html"
    context_object_name = "posts_list"

    def list(self, request):
        return HttpResponse()

    def get_queryset(self):
        queryset = Post.objects.all().order_by("-created_at")
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PostDetail(DetailView):
    def get(self, request, pk):
        queryset = self.get_queryset(pk)
        return HttpResponse(f"Post Detail: {queryset.content}")

    def get_queryset(self, pk):
        queryset = Post.objects.get(id=pk)
        return queryset

class PostNew(CreateView):
    def put(self, request):
        return HttpResponse("Post New")


class PostEdit(UpdateView):
    def patch(self, request, pk):
        return HttpResponse(f"Post Edit {pk}")


class PostDelete(DeleteView):
    def delete(self, request, pk):
        return HttpResponse(f"Post Delete {pk}")
