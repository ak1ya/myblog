from django.urls import path
from . import views

urlpatterns = [
  path("",views.index,name="index"),
  path("new/",views.new,name="new"),
  path("article/all/", views.article_all, name="article_all"),
  path("article/<int:pk>/",views.view_article,name="view_article"),
]