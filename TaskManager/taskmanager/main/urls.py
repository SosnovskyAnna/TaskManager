from django.urls import path, include
from . import views
import django.contrib.auth

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('create', views.create, name='create'),
    path('edit$<int:id>', views.edit, name='edit'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('delete$<int:id>', views.delete, name='delete')
]