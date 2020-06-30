from django.shortcuts import render, redirect
from .forms import UserForm, PChangeForm
from AccountProfile.forms import UserProfileForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
# from django.contrib.auth.forms import PasswordChangeForm


# Create your views here.



#register view for account creation

def register(request):
	if request.method == 'POST':
		form_user = UserForm(request.POST)
		form_profile = UserProfileForm(request.POST)


		if form_user.is_valid() and form_profile.is_valid():

			user = form_user.save()
			profile= form_profile.save(commit=False)

			profile.user = user

			profile.save()

			messages.success(request, 'your account has been created!. you can now login')
			return redirect('accounts:login')

			# to refresh page

			form_user=UserForm()
			form_profile = UserProfileForm()


	else:
		form_user=UserForm()
		form_profile = UserProfileForm()

	return render(request, 'accounts/signup.html' , {'form_user':form_user, 'form_profile':form_profile})


#view for changing password 

def change_password(request):
	if request.method == 'POST':
		form =PChangeForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('/AllMedia/musicBox')

	else:
		form = PChangeForm(user=request.user)
	return render(request, 'accounts/change-password.html', {'form':form})

