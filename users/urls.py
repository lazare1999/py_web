from django.urls import path
from django.contrib.auth.views import LoginView

from users import views

urlpatterns = [
    path(r'login/$', LoginView.as_view(template_name='users/login.html'), name="login"),
    path(r'^logout/$', views.logout_view, name='logout'),

    path(r'^signup/$', views.signup, name='signup'),
    path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
         views.activate, name='activate'),
]
