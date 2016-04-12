from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^gosl', views.gosl, name='gosl'),
    url(r'^trans', views.trans , name='trans'),
]

