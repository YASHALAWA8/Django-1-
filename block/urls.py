from django.urls import path
from . import views
from block.views import register_user, LikeView

app_name = 'block'
urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('login_user', views.login_user, name="login"),
    path('logout_user', views.logout_user, name='logout'),
    path('register_user', views.register_user, name='register'),
    path('like/<int:pk>/', LikeView, name='like_post'),
]