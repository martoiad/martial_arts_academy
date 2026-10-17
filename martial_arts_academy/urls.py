from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('martial-arts/', include('martial_arts.urls')),
    path('events/', include('events.urls')),
]