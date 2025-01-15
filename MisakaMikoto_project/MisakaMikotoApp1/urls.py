from django.urls import re_path  # Import re_path for regex patterns
from MisakaMikotoApp1 import views

app_name = 'MisakaMikotoApp1'

urlpatterns = [
    re_path(r'^$', views.index, name='index'),  # Use re_path for the root URL
    re_path(r'^register/$', views.register, name='register'),  # Use re_path for the register URL
    re_path('registration/<integer>', views.registration_view, name='registration'),  # Use path for the registration URL
    re_path(r'^user_login/$', views.user_login, name='user_login'),  # Use re_path for the user_login URL
]