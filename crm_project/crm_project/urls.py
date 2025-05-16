
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views 
from crm.views import base, about
from userprofile.views import signup


urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/leads/',include('lead.urls')),
    path('dashboard/',include('dashboard.urls')),
    path('dashboard/client_list/',include('client.urls')),
    path('', base, name='index'),
    path('about/', about, name='about'),
    path('signup/', signup, name='signup'),
    path('login/', views.LoginView.as_view(template_name='userprofile/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(),name='logout'),
]
