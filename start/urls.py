from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$', views.show, name='show'),
    url(r'^save/$', views.save, name='save'),#url(r'^makepoll/$', views.MakePoll.as_view(), name='makepoll')
]