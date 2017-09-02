from django.conf.urls import url, include
from . import views

app_name = 'farmdb'

urlpatterns = [
    url(r'^login/', views.login_user, name='login'),
    url(r'^$', views.index, name='index'),
    url(r'^logout', views.logout_user, name='logout'),
    # The actual urls
    # url(r'^$/', views.index, name='index'),
    # url(r'^$/', views.login_user, name='user_login'),
    # url(r'^$/', views.logout_user, name='user_logout'),

]
