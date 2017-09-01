from django.conf.urls import url, include
from . import views

urlpatterns = [
    # Solely for testing. This should always be empty otherwise
    url(r'^login/', views.login_user, name='login'),
    # url(r'^$', views.create_farmer, name='create_farmer'),

    # The actual urls
    # url(r'^$/', views.index, name='index'),
    # url(r'^$/', views.login_user, name='user_login'),
    # url(r'^$/', views.logout_user, name='user_logout'),

]
