# Chords/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('memorize.urls')),  # Include your app's URL configurations
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)