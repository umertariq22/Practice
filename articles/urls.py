from django.conf.urls import url
from . import views


app_name = 'articles'
urlpatterns = [
    url(r'^$',views.main,name='main'),
    url('(?P<pk>\d+)/$',views.view,name='get'),
    url('(?P<pk>\d+)/delete$',views.delete,name='delete'),
    url('(?P<pk>\d+)/edit$',views.edit,name='edit'),
    url(r'new/$',views.new,name='new')
]