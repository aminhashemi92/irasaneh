from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Resaneh, Category
from django.core.paginator import Paginator
from .forms import LocationForm
from django.db.models import Q, Max, Min
from .filters import ResanehFilter
from urllib.parse import urlencode
from hitcount.utils import get_hitcount_model
from hitcount.views import HitCountMixin

# Create your views here.
def resaneh(request, slug=None, page=1):
    if slug:
        category = get_object_or_404(Category, slug=slug, status=True)
        resaneh_list = category.resaneh.filter(status="p").order_by('-publish')

    else:
        category = None
        resaneh_list = Resaneh.objects.filter(status="p").order_by('-publish')

    filter = ResanehFilter(request.GET, queryset=resaneh_list)
    resaneh_list = filter.qs

    paginator = Paginator(resaneh_list,4)
    resanehs = paginator.get_page(page)

    min_price = Resaneh.objects.aggregate(price=Min('price'))
    min_price = int(min_price['price'])
    max_price = Resaneh.objects.aggregate(price=Max('price'))
    max_price = int(max_price['price'])

    data = request.GET.copy()
    if 'page' in data:
        del data['page']


    context ={
        "category" : category,
        "resanehs" : resanehs,
        "filter" : filter,
        "min_price" : min_price,
        "max_price" : max_price,
        "data" : urlencode(data),
        }
    return render(request,"resaneh/resaneh.html", context)



# def category(request,slug,page=1):
#     pass
#     category = get_object_or_404(Category, slug=slug, status=True)
#     resanehs_list = category.resaneh.filter(status="p").order_by('-publish')
#     paginator = Paginator(resanehs_list,2)
#     resanehs = paginator.get_page(page)
#
#     context = {
#         "category" : category,
#         "resanehs" : resanehs,
#
#     }
#     return render(request,"resaneh/category.html", context)


def details(request, slug):
    resaneh = get_object_or_404(Resaneh, slug=slug, status="p")
    place = resaneh.place
    count_hit = True
    # print(place)
    lastresanehs = Resaneh.objects.filter(status="p", place=place).order_by('-publish').exclude(id=resaneh.id)[:5]
    form = LocationForm()
    # print(resaneh.location)
    context ={
    "resaneh" : resaneh,
    "form" : form,
    "lastresanehs" : lastresanehs,
    }
    # hitcount logic
    hit_count = get_hitcount_model().objects.get_for_object(resaneh)
    hits = hit_count.hits
    hitcontext = context['hitcount'] = {'pk': hit_count.pk}
    hit_count_response = HitCountMixin.hit_count(request, hit_count)
    if hit_count_response.hit_counted:
        hits = hits + 1
        hitcontext['hit_counted'] = hit_count_response.hit_counted
        hitcontext['hit_message'] = hit_count_response.hit_message
        hitcontext['total_hits'] = hits
    return render(request, "resaneh/details.html", context)



def search(request, page=1):
    search = request.GET.get('q')
    resanehs_list = Resaneh.objects.filter(Q(detail__icontains = search)| Q(address__icontains = search)| Q(name__icontains = search) | Q(point__icontains = search) | Q(company__name__icontains = search), status="p").order_by('-publish')
    # articles_list = category.articles.filter(status="p").order_by('-publish')
    paginator = Paginator(resanehs_list,2)
    resanehs = paginator.get_page(page)
    context = {
        "resanehs" : resanehs,
        "search" : search,
    }
    return render(request,"resaneh/search.html", context)
