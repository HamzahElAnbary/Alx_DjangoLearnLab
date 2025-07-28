from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # other urls, for example your app urls
    path('', include('bookshelf.urls')),
]
