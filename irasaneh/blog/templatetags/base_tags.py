from django import template
from ..models import Category
# from register_login.models import User

register = template.Library()


@register.simple_tag
def title():
    return "aminhashemi"


@register.inclusion_tag("blog/partials/blog_category_sidebar.html")
def category_sidebar():
    return {
        "category" : Category.objects.filter(status = True),
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
