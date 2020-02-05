from django.shortcuts import render
from django.http import Http404
from . import models

# Create your views here.
def index(request):
  template_name = "blog/index.html" # templates以下のパスを書く(アプリケーション名[blog] / ファイル名[index.html])
  return render(request,template_name)

def new(request):
    template_name = "blog/new.html"
    if request.method == "POST":
        models.Article.objects.create(title=request.POST["title"],text=request.POST["text"])
    return render(request,template_name)    

def article_all(request):
    template_name = "blog/article_all.html"
    context = {"articles":models.Article.objects.all()}
    return render(request,template_name,context)    

def view_article(request,pk):
    template_name = "blog/view_article.html"
    try:
        article = models.Article.objects.get(pk=pk)
    except models.Article.DoesNotExist:
        raise Http404
    context = {"article":article}
    return render(request,template_name,context)    