from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

#
app_name = 'cars'

urlpatterns = [
    path('showall/', views.showall, name='showall'),
    path('upload/', views.upload, name='upload'),
]
