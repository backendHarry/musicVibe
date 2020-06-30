

from django.urls import path
from .views import create, MusicBox, DeleteMusicView, musicPlayList





from django.conf import settings
from django.conf.urls.static import static 


app_name = 'AllMedia'

urlpatterns = [
	path('AllMedia/musicBox/', MusicBox.as_view(), name = 'musicBox'),
    path('AllMedia/delete/<int:pk>', DeleteMusicView.as_view(), name = 'delete'),
    path('AllMedia/create/', create, name = 'create'),
    path('AllMedia/musicBox/musicPlayList/', musicPlayList, name = 'musicPlayList'),

]



if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)