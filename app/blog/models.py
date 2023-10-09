from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(to="Author", on_delete=models.CASCADE)
    comment = models.ForeignKey(
        to="Comment", on_delete=models.CASCADE, null=True, blank=True
    )
    category = models.ManyToManyField(to="Category", through="PostCategory", blank=True)
    tag = models.ManyToManyField(to="Tag", through="PostTag", blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = "Post"


class Author(models.Model):
    name = models.CharField(max_length=20, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "Author"


class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "Category"


class PostCategory(models.Model):
    post = models.ForeignKey(to="Post", on_delete=models.CASCADE)
    category = models.ForeignKey(to="Category", on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "PostCategory"


class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "Tag"


class PostTag(models.Model):
    post = models.ForeignKey(to="Post", on_delete=models.CASCADE)
    tag = models.ForeignKey(to="Tag", on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "PostTag"


class Comment(models.Model):
    author = models.CharField(max_length=20)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.content

    class Meta:
        db_table = "Comment"
