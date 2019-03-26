from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url('^images',views.images,name = 'images'),
    url(r'^new/profile', views.new_profile, name='new-profile'),
    url(r'^search/', views.search_profiles, name='search_profiles'),
    url(r'^new/image', views.image, name='image'), 
    url(r'^comment', views.comment, name='comment'),
    url(r'^likes', views.likes, name='likes'),
     
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)