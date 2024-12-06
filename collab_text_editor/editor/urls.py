from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.homepage, name='homepage'),  # Add a route for the homepage
    path('create/', views.create_document, name='create_document'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('document/<int:pk>/', views.document_detail, name='document_detail'),
    path('register/', views.register, name='register'),
     path('documents/', views.document_list, name='document_list'),  # List all documents
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Login view
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout view
    path('save_comment/', views.save_comment, name='save_comment'),
]
