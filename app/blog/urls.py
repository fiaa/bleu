from django.urls import path
from django.views.generic import RedirectView

from .views import PostDelete, PostDetail, PostEdit, PostList, PostNew

urlpatterns = [
    path("", RedirectView.as_view(url="posts/")),
    path("posts/", PostList.as_view(), name="post_list"),
    path("posts/add/", PostNew.as_view(), name="post_new"),
    path("posts/<int:pk>/", PostDetail.as_view(), name="post_detail"),
    path("posts/<int:pk>/edit/", PostEdit.as_view(), name="post_edit"),
    path("posts/<int:pk>/delete/", PostDelete.as_view(), name="post_delete"),
]
