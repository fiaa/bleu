from django.db import models


class CommonMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(CommonMixin, models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(to="Author", on_delete=models.CASCADE)
    comment = models.ForeignKey(
        to="Comment", on_delete=models.CASCADE, null=True, blank=True
    )
    category = models.ManyToManyField(to="Category", through="PostCategory", blank=True)
    tag = models.ManyToManyField(to="Tag", through="PostTag", blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = "Post"


class Author(CommonMixin, models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "Author"


class Category(CommonMixin, models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "Category"


class PostCategory(CommonMixin, models.Model):
    post = models.ForeignKey(to="Post", on_delete=models.CASCADE)
    category = models.ForeignKey(to="Category", on_delete=models.CASCADE)

    class Meta:
        db_table = "PostCategory"


class Tag(CommonMixin, models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "Tag"


class PostTag(CommonMixin, models.Model):
    post = models.ForeignKey(to="Post", on_delete=models.CASCADE)
    tag = models.ForeignKey(to="Tag", on_delete=models.CASCADE)

    class Meta:
        db_table = "PostTag"


class Comment(CommonMixin, models.Model):
    author = models.CharField(max_length=20)
    content = models.TextField()

    def __str__(self) -> str:
        return self.content

    class Meta:
        db_table = "Comment"
