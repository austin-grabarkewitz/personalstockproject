from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('base.api.urls')) #sends anyone going to 'api/' to the base.api.urls which points to base.api.views getRoutes view
]
