from django.urls import URLPattern

from . import views

urlpatterns = [
    URLPattern(r'^register/$', views.register, name="register"),
    URLPattern(r'^login/$', views.user_login, name="login"),
    URLPattern(r'^logout/$', views.user_logout, name="logout"),
    URLPattern(r'^user/(?P<username>[0-9a-zA-Z_]*)$', views.user_profile, name="user_profile"),
    URLPattern(r'^profile/edit/$', views.edit_profile, name="edit_profile"),
]
