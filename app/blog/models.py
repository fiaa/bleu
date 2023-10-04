from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # 최초 생성 시간
    updated_at = models.DateTimeField(auto_now=True)  # 수정 시간

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)  # 최초 생성 시간
    updated_at = models.DateTimeField(auto_now=True)  # 수정 시간

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)  # 최초 생성 시간
    updated_at = models.DateTimeField(auto_now=True)  # 수정 시간

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)  # 최초 생성 시간
    updated_at = models.DateTimeField(auto_now=True)  # 수정 시간

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # 최초 생성 시간
    updated_at = models.DateTimeField(auto_now=True)  # 수정 시간

    def __str__(self):
        return self.content
