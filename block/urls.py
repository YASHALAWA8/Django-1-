from django.urls import path
from . import views
from block.views import registration

app_name = 'block'
urlpatterns = [
    path('', views.home_page(), name='home_page'),
    path('login_user', views.login_user, name="login"),
    path('logout_user', views.logout_user, name='logout'),
]