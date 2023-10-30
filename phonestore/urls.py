from django.urls import path
from django.contrib.auth import views as authviews  
from . import views


urlpatterns =[

    path('', views.dashboard, name='dashboard'),
    path('customer/<slug:slug>', views.customer, name='customer'),
    
   
    
    path('profile/', views.profile, name='profile'),
    path('phones/', views.phones, name='phones'),
    path('create/', views.create, name='create'),
    path('create_P/<slug:slug>', views.create_P, name='create_P'),
    path('update/<slug:slug>', views.update, name='update'),
    path('delete/<slug:slug>', views.delete, name='delete'),
    path('create_C/', views.create_C, name='create_C'),
    path('update_C/<slug:slug>', views.update_C, name='update_C'),
    path('login/', views.userlogin, name='userlogin'),
    path('register/', views.register, name='register'),
    path('logout/', views.userlogout, name='userlogout'),
    path('profile_info/', views.profile_info, name='profile_info'),

   

   path('password_reset/', authviews.PasswordResetView.as_view(template_name='phonestore/password_reset.html'), name='password_reset'),
   path('reset_password_sent/', authviews.PasswordResetDoneView.as_view(template_name='phonestore/password_reset_sent.html'), name='password_reset_done'),
   path('reset/<uidb64>/<token>', authviews.PasswordResetConfirmView.as_view(template_name='phonestore/password_reset_form.html'), name='password_reset_confirm'),
   path('reset_password_complete/', authviews.PasswordResetCompleteView.as_view(template_name='phonestore/password_reset_done.html'), name='password_reset_complete'),
]
