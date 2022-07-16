from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import Article
from resaneh.models import Resaneh, Category
from .forms import ContactUsForm
from extensions.utils import get_client_ip
from .models import ContactUs
from django.contrib import messages

# Create your views here.
def homepage(request):
    articles = Article.objects.filter(status="p").order_by('-publish')[:4]
    resanehs = Resaneh.objects.filter(status="p", is_digital=False).order_by('-publish')[:4]
    categories = Category.objects.filter(status=True, parent=None)
    allresanehcount = Resaneh.objects.all().count()

    ip_address = get_client_ip(request)

    # try:
    #     contact = ContactUs.objects.get(ip_address=ip_address)
    # except ContactUs.DoesNotExist:
    #     contact = None

    # print(contact)

    form = ContactUsForm()
    # form.fields['ip_address'].initial = ip_address
    if request.POST:
        form = ContactUsForm(request.POST)
        if form.is_valid():
            obj = form.save()
            obj.ip_address = ip_address
            obj.save()
            messages.success(request,'پیام شما با موفقیت ارسال گردید.')
            return redirect('/')

    context ={
        "articles" : articles,
        "resanehs" : resanehs,
        "categories" : categories,
        "allresanehcount" : allresanehcount,
        "form" : form,
        # "contact" : contact,
        }
    return render(request,"home/homepage.html", context)
    # return render(request, "home/homepage.html")


def about(request):
    return render(request, "home/about.html")


def contact(request):
    form = ContactUsForm()
    # form.fields['ip_address'].initial = ip_address
    if request.POST:
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'پیام شما با موفقیت ارسال گردید.')
            # obj.ip_address = ip_address
            # obj.save()
            # return redirect('/')

    context ={
        "form" : form,
        }

    return render(request, "home/contact.html", context)


def faq(request):
    return render(request, "home/faq.html")


def termsAndconditions(request):
    return render(request, "home/termsAndconditions.html")



def whoWeAre(request):
    form = ContactUsForm()
    # form.fields['ip_address'].initial = ip_address
    if request.POST:
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'پیام شما با موفقیت ارسال گردید.')
            # obj.ip_address = ip_address
            # obj.save()
            return redirect('/whoWeAre#contact')

    context ={
        "form" : form,
        }
    return render(request, "home/whoWeAre.html", context)
