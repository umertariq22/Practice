from django.conf.urls import url
from . import views

app_name = 'cbv'
urlpatterns = [
    url(r'^$',views.MainPageView.as_view(),name='index'),
    url(r'^create/',views.CreateArticle.as_view(),name='create'),
    url(r'^(?P<pk>\d+)/$',views.DetailViewArticle.as_view(),name='detail'),
    url(r'^edit/(?P<pk>\d+)/$',views.UpdateViewArticles.as_view(),name='update'),
    url(r'^delete/(?P<pk>\d+)/$',views.DeleteViewArticle.as_view(),name='delete'),
]