from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DeleteView
from .forms import MediaFilesForm
from .models import MediaFiles
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.


@login_required
def create(request):
	if request.method=='POST':
		form = MediaFilesForm(request.POST, request.FILES)
		if form.is_valid():
			files = request.FILES.getlist('files') #getting list of files with description 
			for f in files:
				files_in_db = MediaFiles.objects.filter(user_for_files = request.user).filter(name=f.name).exists()
				if files_in_db: #checking file alreadty exists to avoid users saving twice to db 
					continue
				else:
					MediaFiles.objects.create(name=f.name, files=f, user_for_files=request.user)
	else:
		form = MediaFilesForm()
	context ={
		'form':form
	}
	return render(request, 'AllMedia/create.html', context)

#view to list all my songs to user
class MusicBox(ListView):
	model = MediaFiles
	template_name = 'AllMedia/musicBox.html'
	context_object_name = 'files'

	def get_queryset(self):
		queryset = super(MusicBox, self).get_queryset()
		query = self.request.GET.get('q')
		if query:
			return queryset.filter(user_for_files= self.request.user).filter(name__icontains=query)
		if self.request.user.is_authenticated:
			return queryset.filter(user_for_files = self.request.user)
		else:
			redirect('accounts:register')


class DeleteMusicView(DeleteView):
	model = MediaFiles
	template_name = 'AllMedia/delete_confirm.html'
	success_url = reverse_lazy('AllMedia:musicBox')

	def test_func(self):
		music = Post.get_object()
		if self.request.user == music.user_for_files:
			return True
		return False


#handle Api for use in javascript

def musicPlayList(request):
	list_file = []

	media_files = MediaFiles.objects.filter(user_for_files=request.user)

	for i, j  in enumerate(media_files):
		list_file.append({j.name:j.files.url})

	return JsonResponse(list_file, safe=False)

