from django.http import HttpResponse
from django.shortcuts import redirect
from account.models import Profile

def unathenticated_user(views_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:homepage')
        else:
            return views_func(request, *args, **kwargs)
    return wrapper_func


# just manager can see
def manager_user(views_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.profile.position == 'm':
            return views_func(request, *args, **kwargs)
        else:
            return redirect('dashboard:dashboard')

    return wrapper_func


def allowed_users(allowed_roles = []):
    def decorator(views_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return views_func(request, *args, **kwargs)
            else:
                return HttpResponse('you are not allow')
        return wrapper_func
    return decorator


def profile_complete_needed(views_func):
    def wrapper_func(request, *args, **kwargs):
        user = request.user
        try:
            profile = Profile.objects.get(user=user)
        except Profile.DoesNotExist:
            profile = None

        if profile != None:
            return views_func(request, *args, **kwargs)
        else:
            return redirect('dashboard:profile')

    return wrapper_func
