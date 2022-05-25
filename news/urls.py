from pathlib import Path
from django.conf.urls.static import static
from unicodedata import name
from django.urls import re_path,include
from django.conf import settings
from .import views

urlpatterns=[

    re_path(r'^$',views.news_of_day,name='newsToday'),

    re_path(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name = 'pastNews'),
    
    re_path(r'^search/', views.search_results, name='search_results'),
    
    re_path(r'^article/(\d+)',views.article,name ='article')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

   
