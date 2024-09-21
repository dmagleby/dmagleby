from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls')),
    path('users/', include('users.urls')),
    path('campaigns/', include('campaigns.urls')),
    path('cases/', include('cases.urls')),
]