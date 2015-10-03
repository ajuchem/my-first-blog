from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
] #this will tell Django that views.post_list is the right place to go if someone enters http://127.0.0.1:8000/ as address
