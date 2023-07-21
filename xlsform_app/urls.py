from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views

urlpatterns = [
    url(r'^json_workbook/', views.json_workbook),
    url(r'^$', views.index),
    url(r'^downloads/(?P<path>.*)$', views.serve_file),
    path('api/xform/', views.XFormAPIView.as_view(), name='api-xform'),
]

urlpatterns += staticfiles_urlpatterns()
