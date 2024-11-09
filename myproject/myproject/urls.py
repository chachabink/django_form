from django.contrib import admin
from django.urls import path, include
from subscribe import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('customers/', include('subscribe.urls')),
    path('layanan/', views.layanan, name='layanan'),
]