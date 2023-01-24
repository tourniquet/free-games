from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views


urlpatterns = [
  path('', views.index),
  path('genre/<str:genre>', views.by_genre),
  path('platform/<str:platform>', views.by_platform),
]

if settings.DEBUG:
  urlpatterns += staticfiles_urlpatterns()
