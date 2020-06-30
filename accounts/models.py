from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



# Create your models here.

#model manager for custom user model 
class UserManager(BaseUserManager):

	def create_user(self, email, password=None, is_staff=False, is_admin=False, is_active=True):
		if not email:
			raise ValidationError('user must provide an email')
		user_obj = self.model(
				email=self.normalize_email(email),
			)
		user_obj.set_password(password)
		user_obj.active=is_active
		user_obj.admin=is_admin
		user_obj.staff=is_staff
		user_obj.save(using=self._db)
		return user_obj

	def create_staffuser(self, email, password):
		user = self.create_user(
				email,
				password,
				is_staff = True,
				is_active =True
			)
		return user

	def create_superuser(self, email, password):
		user = self.create_user(
				email,
				password, 
				is_admin= True,
				is_staff=True,
				is_active=True
			)
		return user


class User(AbstractBaseUser):
	email = models.EmailField(unique=True, max_length=255)
	is_active = models.BooleanField(default=True)
	admin = models.BooleanField(default=False)
	staff = models.BooleanField(default=False)


	USERNAME_FIELD= 'email'

	objects = UserManager()

	def get_full_name(self):
		return self.email

	def get_short_name(self):
		return self.email

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True

	@property
	def is_admin(self):
		return self.admin

	@property
	def is_staff(self):
		return self.staff
	