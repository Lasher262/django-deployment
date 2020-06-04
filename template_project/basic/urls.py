
from django.conf.urls import url
from . import views
from django.urls import path
#template tagging 
app_name = 'basic'

urlpatterns = [
	url(r'relative/$',views.relative,name='relative'),
	url(r'other/$',views.other,name='other'),
]