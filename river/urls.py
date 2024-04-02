from django.urls import path
from .views import add_river, show_river, update_river, delete_river


urlpatterns = [
    path('add/', add_river, name='add_url'),
    path('show/', show_river, name='show_url'),
    path('update/<int:pk>/', update_river, name='update_url'),
    path('delete/<int:pk>/', delete_river, name='delete_url'),
]