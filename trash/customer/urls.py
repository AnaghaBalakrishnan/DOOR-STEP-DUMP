from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('h',Userhome.as_view(),name='userh'),
    path('book/<int:bid>',BookingView.as_view(),name='book'),
    path('bookedlist',BookedList.as_view(),name='blist'),
    # path('eb/<int:rid>',Update.as_view(),name='eb'),
    path('dlt/<int:id>',delete,name='dlt')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
