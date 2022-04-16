from django.shortcuts import render, redirect
from django.http import HttpResponse
from account.forms import ProfileForm, CompanyForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import *
from account.models import Profile
from resaneh.models import Resaneh
from hitcount.utils import get_hitcount_model
from hitcount.views import HitCountMixin

# Create your views here.
@login_required
@profile_complete_needed
def dashboard(request):

    company = request.user.profile.company
    employees = Profile.objects.filter(company=company)
    cemployees = employees.count()

    if request.user.profile.position == 'm':
        company = request.user.profile.company
        resanehs = Resaneh.objects.filter(company=company)
        cresanehs = resanehs.count()
        actives = resanehs.filter(status='p').count()

    elif request.user.profile.position == 'c':
        resanehs = Resaneh.objects.filter(creator=request.user)
        cresanehs = resanehs.count()
        actives = resanehs.filter(status='p').count()

    hits = 0
    for resaneh in resanehs:
        hit_count = get_hitcount_model().objects.get_for_object(resaneh)
        hits += hit_count.hits


    context={
    "cemployees" : cemployees,
    "cresanehs" : cresanehs,
    "hits" : hits,
    "actives" : actives,
    }
    return render(request, "dashboard/dashboard.html", context)

#
# def profile(request):
#     return render(request, "dashboard/profile.html")


@login_required
def profile(request):
    user = request.user

    try:
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        profile = None

    if profile != None:
        company = user.profile.company
        form1 = ProfileForm(instance = profile)
        form2 = CompanyForm(instance = company)
        if 'profile' in request.POST:
            form1 = ProfileForm(request.POST, request.FILES, instance=profile)
            if form1.is_valid():
                form1.save()
                messages.success(request,'اطلاعات شما با موفقیت ثبت گردید')
                # return redirect('/dashboard')

        elif 'company' in request.POST:
            form2 = CompanyForm(request.POST, request.FILES, instance=company)
            if form2.is_valid():
                form2.save()
                messages.success(request,'اطلاعات شما با موفقیت ثبت گردید')

        elif 'req' in request.POST:
            profile.status = True
            profile.save()
            return redirect('dashboard:profile')
                # return redirect('/dashboard')
        # update = form.save(commit=False)
    	# 	update.user = request.user
    	# 	update.save()

        context={
        "form1": form1,
        "form2": form2,
        }
        return render(request,"dashboard/profile.html", context)
    else:
        form1 = ProfileForm()
        form2 = CompanyForm()
        if 'profile' in request.POST:
            print("profile")
            form1 = ProfileForm(request.POST, request.FILES, instance=profile)
            if form1.is_valid():
                obj = form1.save()
                obj.user = request.user
                obj.save()
                messages.success(request,'اطلاعات شما با موفقیت ثبت گردید')
                # return redirect('/dashboard')

        elif 'company' in request.POST:
            form2 = CompanyForm(request.POST, request.FILES, instance=company)
            if form2.is_valid():
                form2.save()
                messages.success(request,'اطلاعات شما با موفقیت ثبت گردید')
                # return redirect('/dashboard')
        # update = form.save(commit=False)
    	# 	update.user = request.user
    	# 	update.save()

        context={
        "form1": form1,
        "form2": form2,
        }
        return render(request,"dashboard/profile.html", context)

@login_required
@profile_complete_needed
@manager_user
def employee(request):
    # if request.user.profile.position == 'm':
    company = request.user.profile.company
    employees = Profile.objects.filter(company=company).order_by('-date_created')
    print(employees)

    context={
    "employees": employees,
    }
    return render(request,"dashboard/employee.html", context)

@login_required
@profile_complete_needed
def myresaneh(request):
    if request.user.profile.position == 'm':
        company = request.user.profile.company
        resanehs = Resaneh.objects.filter(company=company).order_by('-publish')

    elif request.user.profile.position == 'c':
        resanehs = Resaneh.objects.filter(creator=request.user).order_by('-publish')
    # print(employees)

    context={
    "resanehs": resanehs,
    }
    return render(request,"dashboard/myresaneh.html", context)
