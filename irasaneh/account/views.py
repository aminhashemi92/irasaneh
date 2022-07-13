from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth import login, logout
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from .forms import *
from .decorators import unathenticated_user
from .models import CustomUser, Profile
from extensions.utils import send_otp



# Create your views here.
@unathenticated_user
def login(request):
    if request.POST :
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        user = authenticate(request, username=phone, password=password)
        if user is not None:
            auth_login(request,user)
            try:
                profile = Profile.objects.get(user=user)
            except Profile.DoesNotExist:
                profile = None

            if profile != None:
                return redirect('/')
            else:
                return redirect('dashboard:profile')
        else:
            messages.info(request, "نام‌کاربری یا رمز عبور اشتباه است!")
            return redirect('account:login')

    return render(request,"account/login.html")


@unathenticated_user
def register(request):
    form = UserAdminCreationForm()
    if request.POST :
        form = UserAdminCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            phone = form.cleaned_data.get('phone')
            messages.success(request, phone + ' کاربر جدید با موفقیت اضافه شد! ' )
            return redirect('account:login')
        else:
            pass
            # messages.info(request, "نام‌کاربری و یا رمزعبور مناسب انتخاب نشده‌است!")
    context={'form':form}
    return render(request,"account/register.html", context)


def logoutUser(request):
    logout(request)
    return redirect('/')

@unathenticated_user
def phoneOtp(request):
    if request.POST :
        phone = request.POST.get('phone')
        try:
            user = CustomUser.objects.get(phone=phone)
        except CustomUser.DoesNotExist:
            user = None
        # user = get_object_or_404(CustomUser, phone=phone)
        if user is not None:
            request.session['phone'] = phone
            return redirect('account:codeOtp')
        else:
            messages.info(request, "کاربری با این شماره‌ی تلفن وجود ندارد")
            return redirect('account:phoneOtp')

    return render(request,"account/phoneOtp.html")
#
@unathenticated_user
def codeOtp(request):
    form = CodeForm(request.POST or None)
    phone = request.session.get('phone')

    phone2 = 'None'
    if phone:
        phone2 = phone[:4] + "****" + phone[8:]
        user = CustomUser.objects.get(phone=phone)
        code = user.code
        code_user = f"{user.code}"
        if not request.POST:
            send_otp(code_user, user.phone)
            # print(code_user)
        if form.is_valid():
            num = form.cleaned_data.get('number')
            if str(code) == num:
                code.save()
                auth_login(request,user)
                try:
                    profile = Profile.objects.get(user=user)
                except Profile.DoesNotExist:
                    profile = None

                if profile != None:
                    return redirect('/')
                else:
                    return redirect('dashboard:profile')

            else:
                messages.info(request, "کد واردشده صحیح نیست!")
                return redirect('account:codeOtp')

    context={
        'phone':phone2,
        'form':form,
    }
    return render(request,"account/codeOtp.html", context)
# @login_required
# def changeprofile(request):
# 	user = request.user
# 	form = UpdateUserForm(instance = user)
# 	if request.method == 'POST':
# 		form = UpdateUserForm(request.POST, request.FILES, instance=request.user)
# 		update = form.save(commit=False)
# 		update.user = request.user
# 		update.save()
# 		messages.success(request,'اطلاعات شما با موفقیت ثبت گردید')
#
# 	context={
# 		"form":form,
# 	}
# 	return render(request,"register_login/changeprofile.html", context)
#
#
# def changepassword(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)  # Important!
#             # messages.success(request, 'پسورد شما با موفقیت تغییر کرد!')
#             return redirect('/')
#         else:
#             messages.error(request, '')
#     else:
#         form = PasswordChangeForm(request.user)
#     return render(request, 'register_login/changepassword.html', {
#         'form': form
#     })
