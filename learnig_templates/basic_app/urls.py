from django.contrib import admin
from django.conf.urls import url
from basic_app import views
app_name = 'basic_app'
#from django.urls import url
urlpatterns = [
    #url(r'^$',views.index,name = "index"),
    url(r'^other/$',views.other, name = "other"),
    url(r'^relative/$',views.relative, name = "relative"),
]
