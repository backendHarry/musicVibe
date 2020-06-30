from .models import UserProfile
from django import forms


TYPE_CHOICES=(
		('Music free', 'Music free'),
		('Music Pro', 'Music Pro')
)


class UserProfileForm(forms.ModelForm):
	musicType = forms.ChoiceField(widget=forms.RadioSelect(), choices=TYPE_CHOICES)

	class Meta:
		model = UserProfile
		fields=['musicType']