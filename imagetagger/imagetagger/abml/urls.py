from django.conf.urls import url

from . import views

app_name = 'abml'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^experiment/create/$', views.create_abmlexperiment,
        name='create_abmlexperiment'),
    url(r'^experiment/(\d+)/$', views.view_abmlexperiment,
        name='view_abmlexperiment')
]
