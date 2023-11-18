from django.contrib import admin

from .models import Author, Category, Comment, Post, PostCategory, PostTag, Tag


class PostCategoryInline(admin.TabularInline):
    model = PostCategory


class PostTagInline(admin.TabularInline):
    model = PostTag


class PostAdmin(admin.ModelAdmin):
    # filter_horizontal = ("tag", "category")
    inlines = [PostCategoryInline, PostTagInline]


admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory)
admin.site.register(PostTag)
