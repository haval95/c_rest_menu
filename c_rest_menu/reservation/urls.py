from django.urls import path
from .views import reserve_view

urlpatterns = [
    path("", reserve_view.as_view(), name="reservation_view"),
]
