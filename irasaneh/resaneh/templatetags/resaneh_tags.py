from django import template
from ..models import Category, Resaneh
from django.db.models import Count
# from register_login.models import User

register = template.Library()


@register.simple_tag
def title():
    return "aminhashemi"


@register.inclusion_tag("resaneh/partials/resaneh_category_sidebar.html")
def category_sidebar():
    category = Category.objects.filter(status = True)
    return {
        "category" : category,
    }


@register.inclusion_tag("resaneh/partials/offer.html")
def offer():
    offer = Resaneh.objects.filter(status='p').order_by('viewed')
    return {
        "offer" : offer[0],
    }


# @register.inclusion_tag("course/postgallery.html")
# def postgallery(id, user):
#     # return "hi"
#     return {
#         "postgallery" : PostGallery.objects.get(pk = id),
#         "user" : user,
#     }
#
# @register.inclusion_tag("course/postvideo.html")
# def postvideo(id, user):
#     # return "hi"
#
#     return {
#         "postvideo" : PostVideo.objects.get(pk = id),
#         "user" : user,
#     }
