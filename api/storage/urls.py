from django.urls import path
from .views import ProductView
urlpatterns = [
    path('list/', ProductView.as_view())
]