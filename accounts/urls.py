from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('accounts/login', views.login_screen, name='login'),
    path('accounts/register', views.register_screen, name='register'),
    path('accounts/logout', views.logout_user, name='logout'),
    path('accounts/medics', views.medics_screen, name='medics'),
    path('accounts/consultation/<int:id>/', views.consultation_screen, name='consultation'),
    path('accounts/myConsults', views.my_consults_screen, name='my_consults'),
]
