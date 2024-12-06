from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import LoginView
from editor import views
from django.shortcuts import redirect

class CustomLoginView(LoginView):
    def get_redirect_url(self):
        # Check for 'next' parameter in GET request, default to '/documents/' if not present
        next_url = self.request.GET.get('next', '/documents/')
        
        # If there is no 'next' parameter, use the LOGIN_REDIRECT_URL
        if not next_url:
            next_url = self.get_success_url()
        
        return next_url

urlpatterns = [
    path('', include('editor.urls')),  # Include the editor URLs for the homepage and create document
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Include Django's auth URLs
    path('accounts/login/', CustomLoginView.as_view(), name='login'),  # Use CustomLoginView for login
]
