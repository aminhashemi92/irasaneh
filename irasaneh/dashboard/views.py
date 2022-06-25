from django.shortcuts import render, redirect
from django.http import HttpResponse
from account.forms import ProfileForm, CompanyForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import *
from account.models import Profile
from resaneh.models import Resaneh
from resaneh.forms import DigitalResanehFrom
from hitcount.utils import get_hitcount_model
from hitcount.views import HitCountMixin
from VOD.forms import *
from VOD.models import *

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


@superuser_required
def vodDashboard(request):
    resanehs = Resaneh.objects.filter(is_digital=True)
    actives = resanehs.filter(status='p').count()
    cemployees = resanehs.filter(is_Androidbox=True).count()
    cresanehs = resanehs.count()
    videos = AdVideo.objects.all().count()
    boxes = AdBox.objects.all().count()
    events = AdEvent.objects.all().count()


    hits = 0
    for resaneh in resanehs:
        hit_count = get_hitcount_model().objects.get_for_object(resaneh)
        hits += hit_count.hits
    context={
    "cemployees" : cemployees,
    "cresanehs" : cresanehs,
    "hits" : hits,
    "actives" : actives,
    "videos" : videos,
    "boxes" : boxes,
    "events" : events,
    }
    return render(request,"dashboard/vodDashboard.html", context)


@superuser_required
def vodResanehs(request):
    resanehs = Resaneh.objects.filter(is_digital=True).order_by('-publish')
    context={
    "resanehs": resanehs,
    }
    return render(request,"dashboard/vodResanehs.html", context)

@superuser_required
def vodResanehAdd(request):
    user = request.user
    form1 = DigitalResanehFrom()
    # form = MyForm(initial={'my_form_field': my_var})
    if request.POST:
        form1 = DigitalResanehFrom(request.POST)
        if form1.is_valid():
            a = form1.save(commit=False)
            a.creator = user
            a.save()
            # form1.save()
            messages.success(request,'اطلاعات شما با موفقیت ثبت گردید')
            return redirect('/dashboard/vodResanehAdd')
    # resanehs = Resaneh.objects.filter(is_digital=True).order_by('-publish')
    # print(len(resanehs))
    context={
    "form1": form1,
    }
    return render(request,"dashboard/vodResanehAdd.html", context)

@superuser_required
def vodResanehUpdate(request, slug):
    user = request.user
    resaneh = Resaneh.objects.get(slug=slug)
    form1 = DigitalResanehFrom(instance = resaneh)
    if request.POST:
        form1 = DigitalResanehFrom(request.POST, instance = resaneh)
        if form1.is_valid():
            a = form1.save(commit=False)
            a.creator = user
            a.save()
            messages.success(request,'اطلاعات شما با موفقیت ثبت گردید')
            # return redirect('/dashboard/vodResanehAdd')

    context={
    "form1": form1,
    }
    return render(request,"dashboard/vodResanehUpdate.html", context)


@superuser_required
def vodResanehDelete(request, pk):
    resaneh = Resaneh.objects.get(id=pk)
    resaneh.delete()
    return redirect('/dashboard/vodResanehs')



@superuser_required
def vodVideos(request):
    videos = AdVideo.objects.all().order_by('-created')
    print(type(videos[0].video))
    context={
    "videos": videos,
    }
    return render(request,"dashboard/vodVideos.html", context)


@superuser_required
def vodVideoAdd(request):
    user = request.user

    form1 = AdVideoForm()
    if request.POST:
        form1 = AdVideoForm(request.POST, request.FILES)
        if form1.is_valid():
            a = form1.save(commit=False)
            a.owner = user
            a.save()
            messages.success(request,'اطلاعات شما با موفقیت ثبت گردید')
            return redirect('/dashboard/vodVideoAdd')
    # resanehs = Resaneh.objects.filter(is_digital=True).order_by('-publish')
    # print(len(resanehs))
    context={
    "form1": form1,
    }
    return render(request,"dashboard/vodVideoAdd.html", context)

@superuser_required
def vodVideoUpdate(request, pk):
    user = request.user
    video = AdVideo.objects.get(id=pk)
    form1 = AdVideoForm(instance = video)
    if request.POST:
        form1 = AdVideoForm(request.POST, request.FILES, instance = video)
        if form1.is_valid():
            a = form1.save(commit=False)
            a.owner = user
            a.save()
            messages.success(request,'اطلاعات شما با موفقیت ثبت گردید')
            # return redirect('/dashboard/vodResanehAdd')

    context={
    "form1": form1,
    }
    return render(request,"dashboard/vodVideoUpdate.html", context)

@superuser_required
def vodVideoDelete(request, pk):
    video = AdVideo.objects.get(id=pk)
    video.delete()
    return redirect('/dashboard/vodVideos')



@superuser_required
def vodBoxes(request):
    boxes = AdBox.objects.all().order_by('-created')
    context={
    "boxes": boxes,
    }
    return render(request,"dashboard/vodBoxes.html", context)

@superuser_required
def vodBoxAdd(request):
    form1 = AdBoxForm()
    if request.POST:
        form1 = AdBoxForm(request.POST, request.FILES)
        if form1.is_valid():
            form1.save()
            messages.success(request,'اطلاعات شما با موفقیت ثبت گردید')
            return redirect('/dashboard/vodBoxAdd')
    # resanehs = Resaneh.objects.filter(is_digital=True).order_by('-publish')
    # print(len(resanehs))
    context={
    "form1": form1,
    }
    return render(request,"dashboard/vodBoxAdd.html", context)

@superuser_required
def vodBoxUpdate(request, pk):
    box = AdBox.objects.get(id=pk)
    form1 = AdBoxForm(instance = box)
    if request.POST:
        form1 = AdBoxForm(request.POST, instance = box)
        if form1.is_valid():
            form1.save()
            # a = form1.save(commit=False)
            # a.save()
            messages.success(request,'اطلاعات شما با موفقیت ثبت گردید')
            # return redirect('/dashboard/vodResanehAdd')

    context={
    "form1": form1,
    }
    return render(request,"dashboard/vodBoxUpdate.html", context)


@superuser_required
def vodBoxDelete(request, pk):
    box = AdBox.objects.get(id=pk)
    box.delete()
    return redirect('/dashboard/vodBoxes')


@superuser_required
def vodEvents(request):
    events = AdEvent.objects.all().order_by('-created')
    context={
    "events": events,
    }
    return render(request,"dashboard/vodEvents.html", context)

@superuser_required
def vodEventAdd(request):
    form1 = AdEventForm()
    if request.POST:
        form1 = AdEventForm(request.POST, request.FILES)
        if form1.is_valid():
            form1.save()
            messages.success(request,'اطلاعات شما با موفقیت ثبت گردید')
            return redirect('/dashboard/vodEventAdd')
    # resanehs = Resaneh.objects.filter(is_digital=True).order_by('-publish')
    # print(len(resanehs))
    context={
    "form1": form1,
    }
    return render(request,"dashboard/vodEventAdd.html", context)

@superuser_required
def vodEventUpdate(request, pk):
    event = AdEvent.objects.get(id=pk)
    form1 = AdEventForm(instance = event)
    if request.POST:
        form1 = AdEventForm(request.POST, instance = event)
        if form1.is_valid():
            form1.save()
            # a = form1.save(commit=False)
            # a.save()
            messages.success(request,'اطلاعات شما با موفقیت ثبت گردید')
            # return redirect('/dashboard/vodResanehAdd')

    context={
    "form1": form1,
    }
    return render(request,"dashboard/vodEventUpdate.html", context)


@superuser_required
def vodEventDelete(request, pk):
    event = AdEvent.objects.get(id=pk)
    event.delete()
    return redirect('/dashboard/vodEvents')
