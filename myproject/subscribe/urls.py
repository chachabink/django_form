from django.urls import path
from subscribe import views

urlpatterns = [
    path('',views.customers, name='customers'),
]