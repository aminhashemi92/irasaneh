from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article
from resaneh.models import Resaneh, Category

# Create your views here.
def homepage(request):
    articles = Article.objects.filter(status="p").order_by('-publish')[:4]
    resanehs = Resaneh.objects.filter(status="p").order_by('-publish')[:4]
    categories = Category.objects.filter(status=True, parent=None)
    allresanehcount = Resaneh.objects.all().count()

    context ={
        "articles" : articles,
        "resanehs" : resanehs,
        "categories" : categories,
        "allresanehcount" : allresanehcount,
        }
    return render(request,"home/homepage.html", context)
    # return render(request, "home/homepage.html")


def about(request):
    return render(request, "home/about.html")


def contact(request):
    return render(request, "home/contact.html")


def faq(request):
    return render(request, "home/faq.html")
