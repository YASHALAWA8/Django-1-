from django.urls import path
from . import views
from block.views import registration

app_name = 'block'
urlpatterns = [
    path('', views.home_page(), name='home_page'),
    path('user/registration/', registration)
]