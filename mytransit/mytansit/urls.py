from django.urls import path
from . import views

urlpatterns = [
  path('signup/', views.signup, name='signup'),
  path('login/', views.login_view, name="login"),
  path('homepage/', views.index, name='index'),
  path('logout/', views.logout_view, name="logout"),
  path('user/<int:id>/', views.user_info, name='user_info'),
  path('user/<int:id>/edit', views.user_edit, name='user_edit'),
  ]
