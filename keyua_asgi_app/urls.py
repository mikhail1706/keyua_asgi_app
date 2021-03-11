from django.contrib import admin
from django.urls import path, include

api_urlpatters = [
    path('cities/', include('keyua_asgi_app.apps.cities.api.urls'))
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urlpatters))
]
