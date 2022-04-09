from django.shortcuts import render, redirect
# from django.contrib.auth import login, logout
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from .forms import UserAdminCreationForm
from .decorators import unathenticated_user
from .models import CustomUser




# Create your views here.
# @unathenticated_user
def login_register(request):
    form = UserAdminCreationForm()
    # if request.method == 'POST':
    #     phone = request.POST.get('phone')
    #     password = request.POST.get('password')
    #     user = authenticate(request, username=phone, password=password)
    #     if user is not None:
    #         login(request,user)
    #         return redirect('/')
    if(len(request.POST) == 3):
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        user = authenticate(request, username=phone, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.info(request, "نام‌کاربری یا رمز عبور اشتباه است!")
            return redirect('account:login_register')
    elif(len(request.POST) == 4):
        form = UserAdminCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            phone = form.cleaned_data.get('phone')
            messages.success(request, phone + ' کاربر جدید با موفقیت اضافه شد! ' )
            return redirect('account:login_register')
        else:
            messages.info(request, "نام کاربری یا ایمیل تکراری می‌باشد و یا رمز عبور مناسب انتخاب نشده‌است!")
			# messages.info(request, "نام‌کاربری تکراری می‌باشد و یا رمز عبور مناسب انتخاب نشده‌است.")

    # form = CreateUserForm()
	# if request.method == 'POST':
	# 	if(len(request.POST) == 3):
	# 		username = request.POST.get('username')
	# 		password = request.POST.get('password')
	# 		user = authenticate(request, username=username, password=password)
	# 		if user is not None:
	# 			login(request,user)
	# 			return redirect('/')
	# 		else:
	# 			messages.info(request, "نام‌کاربری یا رمز عبور اشتباه است!")
	# 			return redirect('register_login:register_login')
	# 	elif(len(request.POST) == 5):
	# 		form = CreateUserForm(request.POST)
	# 		if form.is_valid():
	# 			user = form.save()
	# 			username = form.cleaned_data.get('username')
	# 			messages.success(request,'کاربر جدید با موفقیت اضافه شد!' + username)
	# 			return redirect('register_login:register_login')
	# 		else:
	# 			# messages.info(request, "نام‌کاربری تکراری می‌باشد و یا رمز عبور مناسب انتخاب نشده‌است.")
	# 			messages.info(request, "نام کاربری یا ایمیل تکراری می‌باشد و یا رمز عبور مناسب انتخاب نشده‌است!")


    context={'form':form}
    return render(request,"account/login_register.html", context)
	# return render(request,"account/login_register.html")


# def register_login(request):
# 	context={}
# 	return render(request,"register_login/register_login.html", context)

def logoutUser(request):
    logout(request)
    return redirect('/')

#
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
