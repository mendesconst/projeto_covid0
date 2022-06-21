from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('premio/<int:id>', views.premio, name='premio'),
]
