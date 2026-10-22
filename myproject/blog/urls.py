from django.urls import path
from . import views
from ..myproject.urls import urlpatterns

urlpatterns[
    path("", views.home, name = "blog_home"),
    path("posts/", views.posts, name = "blog_posts")
]