from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.home),
    path('status/',views.status),
    path('calls/',views.calls)
]
