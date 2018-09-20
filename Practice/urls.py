from django.contrib import admin
from django.conf.urls import url,include
from articles import views
urlpatterns = [
    url(r'^$',views.main,name='main'),
    url(r'^admin/',admin.site.urls,name='admin'),
    url(r'^articles/',include('articles.urls',namespace='articles')),
    url(r'^cbv/',include('cbv.urls',namespace='cbv')),
    url(r'^User/',include('User.urls',namespace='User')),

]
