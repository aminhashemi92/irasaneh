from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article, Category
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils.translation import activate

# Create your views here.
def blog(request, page=1):
    articles_list = Article.objects.filter(status="p").order_by('-publish')
    paginator = Paginator(articles_list,15)
    # page = request.GET.get('page')
    articles = paginator.get_page(page)
    context ={
        "articles" : articles,
        # "rate" : rate_list,
        }
    return render(request,"blog/blog.html", context)
    # return render(request, "blog/blog.html")
    # return HttpResponse("blog")
#
def single(request,slug):

    article = get_object_or_404(Article, slug=slug, status="p")

    ip_address = request.user.ip_address
    if ip_address not in article.hits.all():
        article.hits.add(ip_address)

    lastarticles = Article.objects.filter(status="p").order_by('-publish').exclude(id=article.id)[:4]
    tags = Category.objects.filter(status=True).all()
    print(len(tags))
    context = {
        "article" : article,
        "lastarticles" : lastarticles,
        "tags" : tags,
    }
    return render(request,"blog/single.html", context)



def category(request,slug,page=1):
    category = get_object_or_404(Category, slug=slug, status=True)
    articles_list = category.articles.filter(status="p").order_by('-publish')
    paginator = Paginator(articles_list,15)
    articles = paginator.get_page(page)
    context = {
        "category" : category,
        "articles" : articles,
    }
    return render(request,"blog/category.html", context)


def search(request, page=1):
    search = request.GET.get('q')
    articles_list = Article.objects.filter(Q(minidescription__icontains = search) | Q(description__icontains = search) | Q(title__icontains = search), status="p").order_by('-publish')
    # articles_list = category.articles.filter(status="p").order_by('-publish')
    paginator = Paginator(articles_list,15)
    articles = paginator.get_page(page)
    context = {
        "articles" : articles,
        "search" : search,
    }
    return render(request,"blog/search.html", context)
