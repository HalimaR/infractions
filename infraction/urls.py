from django.urls import path
from . import views

app_name = 'infraction'

urlpatterns = [
    path('<int:speed>/', views.zoeken, name='speed'),
]
