from django.conf.urls import url, include
from . import views

app_name = 'farmdb'

urlpatterns = [
    url(r'^login/', views.login_user, name='login'),
    url(r'^$', views.index, name='index'),
    url(r'^logout', views.logout_user, name='logout'),
    url(r'^create/AnimalGroup$', views.AnimalGroupCreateView.as_view(), name="AnimalGroupCreate"),
    url(r'^list/AnimalGroup$', views.AnimalGroupListView.as_view(), name='AnimalGroupList'),

    # url(r'^$/', views.index, name='index'),
    # url(r'^$/', views.login_user, name='user_login'),
    # url(r'^$/', views.logout_user, name='user_logout'),

]
