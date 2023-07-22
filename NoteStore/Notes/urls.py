from django.urls import path
from . import views
import django.contrib.auth.views as auth_views

app_name='Notes'
urlpatterns = [
path('', views.index, name="index"),
path('login/',auth_views.LoginView.as_view(template_name='frotend/login.html'), name="login"),
path('register/', views.Register, name="Register"),
path('logged/', views.Logged, name="Logged"),
path('logout/', auth_views.LogoutView.as_view(template_name='frotend/logout.html'), name="logout"),
path('update/', views.logout, name="update"),
]
