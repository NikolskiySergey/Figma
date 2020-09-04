from django.urls import path

from . import views

app_name = "figma"
urlpatterns = [
    path('', views.index, name='index'),
    path('base_list.html', views.base_list, name='base_list'),

]

