from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
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
from django.utils import timezone
import plotly.express as px
from collections import Counter
from extensions.utils import jalali_converter2, Persian_numbers_converter, gregorian_converter
from datetime import datetime, timedelta
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


    context={
    "employees": employees,
    }
    return render(request,"dashboard/employee.html", context)

@login_required
@profile_complete_needed
def myofflineresaneh(request):
    if request.user.profile.position == 'm':
        company = request.user.profile.company
        resanehs = Resaneh.objects.filter(company=company, is_digital=False).order_by('-publish')

    elif request.user.profile.position == 'c':
        resanehs = Resaneh.objects.filter(creator=request.user, is_digital=False).order_by('-publish')
    # print(employees)

    context={
    "resanehs": resanehs,
    }
    return render(request,"dashboard/myofflineresaneh.html", context)

@login_required
@profile_complete_needed
def mydigitalresaneh(request):
    if request.user.profile.position == 'm':
        company = request.user.profile.company
        resanehs = Resaneh.objects.filter(company=company, is_digital=True).order_by('-publish')

    elif request.user.profile.position == 'c':
        resanehs = Resaneh.objects.filter(creator=request.user, is_digital=True).order_by('-publish')
    # print(employees)

    context={
    "resanehs": resanehs,
    }
    return render(request,"dashboard/mydigitalresaneh.html", context)


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
            # return redirect('/dashboard/VideoAdd')
            return JsonResponse({'data':'Data Uploaded'})
        else:
            return JsonResponse({'data':'Wrong'})
    context={

        'form1': form1,
    }
    # return render(request, 'dashboard/progress.html', context)
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
    user = request.user
    form1 = AdBoxForm()
    if request.POST:
        form1 = AdBoxForm(request.POST, request.FILES)
        if form1.is_valid():
            a = form1.save()
            videos = a.videos
            a.owner = user
            video_id_list = list(videos.values_list('id', flat=True))
            orders = a.order
            orders_list = map(int, orders.split('-'))
            z = [x for _,x in sorted(zip(orders_list,video_id_list))]
            video_play_list = ','.join(map(str, z))
            a.videos_list = video_play_list
            a.save()

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
    user = request.user
    box = AdBox.objects.get(id=pk)
    form1 = AdBoxForm(instance = box)
    if request.POST:
        form1 = AdBoxForm(request.POST, instance = box)
        if form1.is_valid():
            a = form1.save()
            a.owner = user
            a.save()
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
    user = request.user
    form1 = AdEventForm()
    if request.POST:
        form1 = AdEventForm(request.POST, request.FILES)
        if form1.is_valid():
            a = form1.save(commit=False)
            a.owner = user
            a.save()
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
    user = request.user
    event = AdEvent.objects.get(id=pk)
    form1 = AdEventForm(instance = event)
    if request.POST:
        form1 = AdEventForm(request.POST, instance = event)
        if form1.is_valid():
            a = form1.save(commit=False)
            a.owner = user
            a.save()
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


def charts(request):
    user = request.user
    profile = user.profile
    if profile.position == 'c':
        videos = user.advideo.all()
    elif profile.position == 'm':
        if profile.company:
            videos = profile.company.advideo.all()
        else:
            videos = user.advideo.all()

    boxes = AdBox.objects.filter(videos__in=videos)
    events = AdEvent.objects.filter(media__in=boxes)

    resanehs_id = events.values_list('resaneh', flat=True).distinct()

    resanehs = Resaneh.objects.filter(id__in = resanehs_id)

    qs = AdVideoCounterLog.objects.filter(created__gte=datetime.now()-timedelta(days=7)).filter(resaneh__in=resanehs).filter(video__in=videos)

    qs = qs.order_by('created')
    qs = qs.values_list('created', flat=True).distinct()
    video_list = qs.values_list('video', flat=True).distinct()
    days = [x.date() for x in qs]
    days = [jalali_converter2(x) for x in qs]
    # MyList = AdVideoCounterLog.objects.values('created')
    # MyList = ["a", "b", "a", "c", "c", "a", "c"]
    days_counter = dict(Counter(days))
    counter = list(days_counter.values())
    # print(type(counter[0]))
    day = list(days_counter.keys())


    # print(a)
    # da = []
    # for d in vc:
    #     dd = d.created.date()
    #     if dd not in da:
    #         da.append(dd)
    #
    # ca = []
    # for i in da:
    #     c = vc.filter(created__contains=i).count()
    #     ca.append(c)
    # print(type(da[0]))



    # print(type(vc[0].created.date()))
    # print(vc[0].created.date())
    fig = px.bar(
        x = day,
        y = counter,
        # color=day,
        # color_discrete_sequence=["yellow", ],
        title="تعداد بازدید ویدیو‌ها",
        # x=[c.created.date() for c in vc],
        # y=[c.created.date() for c in vc],
    )

    fig.add_scatter(x=day,y=counter)
    # fig.add_bar(x=day,y=counter)

    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis_title="روز",
        yaxis_title="تعداد بازید",
        showlegend=False,
        hovermode=False,
        font_family="Shabnam",
        title={
            'font_size':22,
            'xanchor':'center',
            'x':0.5,
        }
        # bgcolor='rgba(255, 255, 255, 0)',
        # bordercolor='rgba(255, 255, 255, 0)'
        # ),
        # barmode='group',
        # bargap=0.15, # gap between bars of adjacent location coordinates.
        # bargroupgap=0.1,
    )
    fig.update_xaxes(showline=True, linewidth=2, linecolor='gray')
    fig.update_yaxes(showline=True, linewidth=2, gridcolor='gray')

    fig.update_traces(marker_color='rgb(105,208,221)', marker_line_color='rgb(23,162,184)',
                  marker_line_width=1.5, opacity=0.6,)

    chart = fig.to_html()
    context={
        'chart':chart,
        'videos':videos,
        'resanehs':resanehs,
    }
    # print(vc.count())
    return render(request, "dashboard/charts.html", context)



def load_counterChart(request):
    user = request.user
    profile = user.profile
    if profile.position == 'c':
        videos = user.advideo.all()
    elif profile.position == 'm':
        if profile.company:
            videos = profile.company.advideo.all()
        else:
            videos = user.advideo.all()

    boxes = AdBox.objects.filter(videos__in=videos)
    events = AdEvent.objects.filter(media__in=boxes)

    resanehs_id = events.values_list('resaneh', flat=True).distinct()

    resanehs = Resaneh.objects.filter(id__in = resanehs_id)

    qs = AdVideoCounterLog.objects.filter(resaneh__in=resanehs).filter(video__in=videos)


    if request.GET:
        margin = request.GET.get("margin")
        video = request.GET.get("video")
        media = request.GET.get("media")
        start = request.GET.get("start")
        end = request.GET.get("end")
        if margin:
            if margin == "30_days_ago":
                qs = qs.filter(created__gte=datetime.now()-timedelta(days=30))
            if margin == "7_days_ago":
                qs = qs.filter(created__gte=datetime.now()-timedelta(days=7))
            if margin == "yesterday":
                qs = qs.filter(created__date=datetime.now()-timedelta(days=1))
            if margin == "today":
                qs = qs.filter(created__gte=datetime.now()-timedelta(days=0))

        if start and end:
            start = gregorian_converter(start)
            end = gregorian_converter(end)
            qs = qs.filter(created__gte=start, created__lte=end)
            # print(gregorian_converter(start))
            # print("salam")

        if video:
            qs = qs.filter(video__id__exact=video)
            # qs = AdVideoCounterLog.objects.filter(video__id__contains=video)


        if media:
            qs = qs.filter(resaneh__id__exact=media)
            # qs = AdVideoCounterLog.objects.filter(created__gte=start)
            # qs = AdVideoCounterLog.objects.filter(video=15)
            # qs = AdVideoCounterLog.objects.filter(video=16)
            # print(qs)
            # print(qs)

        # if start:
        #     qs = AdVideoCounterLog.objects.all().order_by('created')
        # if end:
        #     qs = AdVideoCounterLog.objects.all().order_by('created')
    # else:
    #     qs = AdVideoCounterLog.objects.all().order_by('created')
    qs = qs.order_by('created')
    qs = qs.values_list('created', flat=True).distinct()
    days = [x.date() for x in qs]
    days = [jalali_converter2(x) for x in qs]
    # MyList = AdVideoCounterLog.objects.values('created')
    # MyList = ["a", "b", "a", "c", "c", "a", "c"]
    days_counter = dict(Counter(days))
    counter = list(days_counter.values())
    # print(type(counter[0]))
    day = list(days_counter.keys())


    # print(a)
    # da = []
    # for d in vc:
    #     dd = d.created.date()
    #     if dd not in da:
    #         da.append(dd)
    #
    # ca = []
    # for i in da:
    #     c = vc.filter(created__contains=i).count()
    #     ca.append(c)
    # print(type(da[0]))



    # print(type(vc[0].created.date()))
    # print(vc[0].created.date())
    fig = px.bar(
        x = day,
        y = counter,
        # color=day,
        # color_discrete_sequence=["yellow", ],
        title="تعداد بازدید ویدیو‌ها",
        # x=[c.created.date() for c in vc],
        # y=[c.created.date() for c in vc],
    )

    fig.add_scatter(x=day,y=counter)
    # fig.add_bar(x=day,y=counter)

    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis_title="روز",
        yaxis_title="تعداد بازید",
        showlegend=False,
        hovermode=False,
        font_family="Shabnam",
        title={
            'font_size':22,
            'xanchor':'center',
            'x':0.5,
        }
        # bgcolor='rgba(255, 255, 255, 0)',
        # bordercolor='rgba(255, 255, 255, 0)'
        # ),
        # barmode='group',
        # bargap=0.15, # gap between bars of adjacent location coordinates.
        # bargroupgap=0.1,
    )
    fig.update_xaxes(showline=True, linewidth=2, linecolor='gray')
    fig.update_yaxes(showline=True, linewidth=2, gridcolor='gray')

    fig.update_traces(marker_color='rgb(105,208,221)', marker_line_color='rgb(23,162,184)',
                  marker_line_width=1.5, opacity=0.6,)

    chart = fig.to_html()
    context={'chart':chart}
    # print(vc.count())
    return render(request, "dashboard/counterChart.html", context)


def chartjs(request):
    return render(request, "dashboard/chartjs.html")

def flot(request):
    return render(request, "dashboard/flot.html")

def inline(request):
    return render(request, "dashboard/inline.html")





def Videos(request):
    user = request.user
    profile = user.profile
    if profile.position == 'm':
        videos = AdVideo.objects.filter(company=profile.company).order_by('-created')
    elif profile.position == 'c':
        videos = AdVideo.objects.filter(owner=user).order_by('-created')


    context={
    "videos": videos,
    }
    return render(request,"dashboard/Videos.html", context)



def VideoAdd(request):
    user = request.user
    company = user.profile.company
    form1 = AdVideoFormCustomer()
    if request.POST:
        form1 = AdVideoFormCustomer(request.POST, request.FILES)
        if form1.is_valid():
            a = form1.save(commit=False)
            a.owner = user
            a.company = company
            a.save()
            messages.success(request,'اطلاعات شما با موفقیت ثبت گردید')
            return JsonResponse({'data':'Data Uploaded'})
        else:
            msg = form1.errors.as_data()
            print(msg)
            # return JsonResponse({'data':msg})
            return JsonResponse({'data':str(msg)})
            # return redirect('/dashboard/VideoAdd')
    # resanehs = Resaneh.objects.filter(is_digital=True).order_by('-publish')
    # print(len(resanehs))
    context={
    "form1": form1,
    }

    return render(request,"dashboard/VideoAdd.html", context)


def VideoUpdate(request, pk):
    user = request.user
    video = AdVideo.objects.get(id=pk)
    form1 = AdVideoFormCustomer(instance = video)
    if request.POST:
        form1 = AdVideoFormCustomer(request.POST, request.FILES, instance = video)
        if form1.is_valid():
            a = form1.save(commit=False)
            a.owner = user
            a.save()
            messages.success(request,'اطلاعات شما با موفقیت ثبت گردید')
        else:
            print(form1.errors.as_data())
            # return redirect('/dashboard/vodResanehAdd')

    context={
    "form1": form1,
    }
    return render(request,"dashboard/VideoUpdate.html", context)


def VideoDelete(request, pk):
    video = AdVideo.objects.get(id=pk)
    video.delete()
    return redirect('/dashboard/Videos')
