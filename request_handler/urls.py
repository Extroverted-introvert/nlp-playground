from django.urls import path, include, re_path
from django.conf.urls import url
from django.views.static import serve
from django.views.generic import TemplateView

from . import views
app_name = 'request_handler'
urlpatterns = [
    path('', views.MainView.as_view(), name='dashboard'),
]