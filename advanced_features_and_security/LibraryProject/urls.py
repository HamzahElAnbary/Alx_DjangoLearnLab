from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Your app urls
    path('', include('bookshelf.urls')),

    # Add Django auth URLs for login/logout
    path('accounts/', include('django.contrib.auth.urls')),
]
