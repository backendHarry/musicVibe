from django import forms 
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
	UserCreationForm, 
	AuthenticationForm, 
	ReadOnlyPasswordHashField,
	PasswordResetForm,
	PasswordChangeForm
	)


User=get_user_model() #getting my default user


# form for admin admin 

class UserAdminCreationForm(forms.ModelForm):
	password1 = forms.CharField(label ='password', widget=forms.PasswordInput())
	password2 = forms.CharField(label ='confirm password', widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ['email']

	def clean_password2(self):

		password1 = forms.cleaned_data.get('password1')
		password2 = forms.cleaned_data.get('password2')

		if password1 and password2 and password1 != password2:
			raise ValidationError('passwords do not match')
		return password2

	def save(self, commit=True):
		user = super(UserAdminCreationForm, self).save(commit=False)
		user.set_password(self.cleaned_data['password1'])

		if commit:
			user.save()
		return user


class UserAdminChangeForm(forms.ModelForm):
	password = ReadOnlyPasswordHashField()

	class Meta:
		model = User
		fields=['email', 'password', 'is_active', 'admin']

	def clean_password(self):
		return self.initial['password']

# end form admin

#using user_creation form from django forms 

class UserForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['email', 'password1', 'password2']

	def __init__(self, *args, **kwargs):
		super(UserForm, self).__init__(*args, **kwargs)
		#overriding default style for my forms only 

		self.fields['email'].widget.attrs['class'] = 'form-input'
		self.fields['password1'].widget.attrs['class'] = 'form-input'
		self.fields['password2'].widget.attrs['class'] = 'form-input'
		#for placeholders
		self.fields['email'].widget.attrs['placeholder'] = 'username'
		self.fields['email'].widget.attrs['placeholder'] = 'email'
		self.fields['password1'].widget.attrs['placeholder'] = 'password'
		self.fields['password2'].widget.attrs['placeholder'] = 'confirm password'


#using default authentication django forms 

class LoginForm(AuthenticationForm):
	def __init__(self, *args, **kwargs):
		super(LoginForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs['class'] = 'form-input' #overwriting my form fields for styles 
		self.fields['password'].widget.attrs['class'] = 'form-input'

		self.fields['username'].widget.attrs['placeholder'] = 'login with email'
		self.fields['password'].widget.attrs['placeholder'] = 'enter password'


#reset forms 
class ResetForm(PasswordResetForm):
	def __init__(self, *args, **kwargs):
		super(ResetForm, self).__init__(*args, **kwargs)
		self.fields['email'].widget.attrs['class'] = 'form-input'

		self.fields['email'].widget.attrs['placeholder'] = 'Enter your email'

#default to change forms 

class PChangeForm(PasswordChangeForm):
	def __init__(self, *args, **kwargs):
		super(PChangeForm, self).__init__(*args, **kwargs)
		self.fields['old_password'].widget.attrs['class'] = 'form-input'
		self.fields['new_password1'].widget.attrs['class'] = 'form-input'
		self.fields['new_password2'].widget.attrs['class'] = 'form-input'

		self.fields['old_password'].widget.attrs['placeholder'] = 'Enter your old passsword'
		self.fields['new_password1'].widget.attrs['placeholder'] = 'Enter your new passsword '
		self.fields['new_password2'].widget.attrs['placeholder'] = 'enter new password to confirm'