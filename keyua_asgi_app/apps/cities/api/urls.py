from django.urls import path
from .views import UpdateCityApiView


urlpatterns = [
    path('update/<int:city_id>/', UpdateCityApiView.as_view())
]
