from django.shortcuts import render
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.show_main, name = 'main'),
    path('poets/', views.show_poets, name = 'poets'),
    path('poems/', views.show_list_poems, name = 'list_poems'),
    path('poets/<int:poet_id>', views.show_poems, name = 'poems'),
    path('poems/<int:arg1>', views.display_poem, name = 'display_poem'),
    path('poems/<int:arg1>/<str:arg2>', views.display_searched, name = 'display_searched'),
    path('poems/<int:arg1>/popular', views.display_popular, name = 'display_popular'),
    path('poems/<int:arg1>/new', views.display_new, name = 'display_new'),
    path('all_poems/<int:arg1>/<str:search_text>', views.show_searched_again, name = 'show_searched_again'),
    path('all_poems/', views.show_searched, name = 'show_searched'),
    path('poems/show/<int:arg1>', views.create_comment, name = 'create_comment'),
    path('vote/<int:arg1>', views.vote, name = 'vote'),
    path('new_poems/', views.show_new, name = 'show_new'),
    path('popular_poems/', views.show_popular, name = 'show_popular'),
    path('golden_century/', views.golden_century, name = 'golden_century'),
    path('silver_century/', views.silver_century, name = 'silver_century'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)