from django.conf.urls import url
from . import views
app_name = 'User'

urlpatterns = [
    url(r'^signup/$',views.signup,name='signup'),
    url(r'^signin/$',views.login,name='signin')
]