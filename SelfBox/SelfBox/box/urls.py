from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
#from .views import (IndexView)
urlpatterns = [

    path('', views.home_page, name='homepage'),
    path('create', views.simple_upload, name='create'),
    path('Delete', views.delete, name='delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)