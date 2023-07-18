from django.urls import path
from . import views
#create your urls here
app_name='accounts'

urlpatterns = [
    path('register',views.register,name='register'),
    path('login', views.loginview, name='login'),
]