from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^code_and_create/', views.code_and_create, name='code_and_create'),
]