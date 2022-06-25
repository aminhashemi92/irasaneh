from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Resaneh, Category
from django.core.paginator import Paginator
from .forms import LocationForm
from django.db.models import Q, Max, Min
from .filters import ResanehFilter, ResanehSearchFilter
from urllib.parse import urlencode
from hitcount.utils import get_hitcount_model
from hitcount.views import HitCountMixin
from cities.models import Country
from django.core import serializers
from json import dumps
# Create your views here.
def resaneh(request, slug=None, page=1):
    if slug:
        category = get_object_or_404(Category, slug=slug, status=True)
        resaneh_list = category.resaneh.filter(status="p", is_digital=False).order_by('-publish')

    else:
        category = None
        resaneh_list = Resaneh.objects.filter(status="p", is_digital=False).order_by('-publish')

    filter = ResanehFilter(request.GET, queryset=resaneh_list)
    resaneh_list = filter.qs

    paginator = Paginator(resaneh_list,16)
    resanehs = paginator.get_page(page)

    min_price = Resaneh.objects.aggregate(price=Min('price'))
    min_price = int(min_price['price'])
    max_price = Resaneh.objects.aggregate(price=Max('price'))
    max_price = int(max_price['price'])

    data = request.GET.copy()
    if 'page' in data:
        del data['page']

    countries = Country.objects.all()
    context ={
        "category" : category,
        "resanehs" : resanehs,
        "filter" : filter,
        "min_price" : min_price,
        "max_price" : max_price,
        "data" : urlencode(data),
        "countries" : countries,

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
    resaneh = get_object_or_404(Resaneh, slug=slug, status="p",is_digital=False)
    place = resaneh.place
    loc = resaneh.location
    loc = loc.split(",")
    print(loc)
    count_hit = True
    # print(place)
    lastresanehs = Resaneh.objects.filter(status="p", place=place,is_digital=False).order_by('-publish').exclude(id=resaneh.id)[:5]
    form = LocationForm()


    context ={
    "resaneh" : resaneh,
    "form" : form,
    "lastresanehs" : lastresanehs,
    "loc" : loc,
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


def comparison(request, slug1=None, slug2=None, slug3=None, slug4=None):
    resanehs =[]
    if slug1:
        resaneh1 = Resaneh.objects.get(slug=slug1)
        category = resaneh1.category.all()
        resanehs.append(resaneh1)
        # resanehs["resaneh1"] = resaneh1
        if slug2:
            resaneh2 = Resaneh.objects.get(slug=slug2)
            # resanehs["resaneh2"] = resaneh2
            if resaneh2 not in resanehs:
                resanehs.append(resaneh2)
            if slug3:
                resaneh3 = Resaneh.objects.get(slug=slug3)
                # resanehs["resaneh3"] = resaneh3
                if resaneh3 not in resanehs:
                    resanehs.append(resaneh3)
                if slug4:
                    resaneh4 = Resaneh.objects.get(slug=slug4)
                    # resanehs["resaneh4"] = resaneh4
                    if resaneh4 not in resanehs:
                        resanehs.append(resaneh4)

    similars = Resaneh.objects.filter(category__in=category, status="p",is_digital=False)
    category = serializers.serialize('json', category)

    context = {
        "resanehs" : resanehs,
        "similars" : similars,
        "category" : category,


    }
    return render(request, "resaneh/comparison.html", context)




def search_similars(request):
    search = request.GET.get('q')
    category = request.GET.get('category')
    category = category.split(",")

    similars = Resaneh.objects.filter(Q(detail__icontains = search)| Q(address__icontains = search)| Q(name__icontains = search) | Q(point__icontains = search) | Q(company__name__icontains = search), status="p", is_digital=False, category__id__in=category)
    context = {
        "similars" : similars,
        "search" : search,
    }
    return render(request,"resaneh/search_similars.html", context)
