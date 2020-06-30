from django.contrib import admin

from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminChangeForm, UserAdminCreationForm
# Register your models here.

User = get_user_model()

# forms set up
class UserAdmin(BaseUserAdmin):

	create_form = UserAdminCreationForm
	change_form = UserAdminChangeForm

	list_display=('email', 'admin')
	list_filter = ('admin', 'staff', 'is_active')

	fieldsets = (
			(None, {'fields':('email', 'password')}),
			('personal info', {'fields':()}),
			('permissions', {'fields':('admin', 'staff', 'is_active')}),
		)

	add_fieldsets =(
			(None, {'classes':('wide',), 
			'fields':('email', 'password1', 'password2')}),
		)

	search_fields = ('email',)
	ordering = ('email',)
	filter_horizontal = ()



# auth
admin.site.register(User, UserAdmin)



