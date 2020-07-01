

from django.urls import path, reverse_lazy, include
from django.contrib.auth import views as Auth_views
from .forms import LoginForm, ResetForm
from .views import register, change_password


app_name = 'accounts'

urlpatterns = [

	path('accounts/register/', register, name = 'register'),

    path('accounts/login/', Auth_views.LoginView.as_view(
        template_name='accounts/login.html', 
        authentication_form=LoginForm, 
        redirect_authenticated_user=False), 
        name = 'login'),

    path('accounts/logout/', Auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name = 'logout'),

    path('accounts/reset-password/',
    	Auth_views.PasswordResetView.as_view( 
    		form_class=ResetForm,
            success_url=reverse_lazy('accounts:password_reset_done'),
            template_name='accounts/reset_password.html',
            email_template_name='accounts/password_reset_email.html'),
    		name = 'password_reset'),

    path('accounts/reset/done/',
            Auth_views.PasswordResetDoneView.as_view(
            template_name = 'accounts/password_reset_done.html'
            ), name="password_reset_done"
        ),

    path('accounts/reset/<uidb64>/<token>/', 
        Auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html'), 
         name="password_reset_confirm"),

    path('accounts/reset_complete/', 
    		Auth_views.PasswordResetCompleteView.as_view(
    		template_name='accounts/password_reset_complete.html'), 
    		name = 'password_reset_complete'),



    path('change-password/', change_password, name = 'change_password'),

]


# template_name='accounts/reset_password.html',
# template_name='accounts/password_reset_confirm.html'), 