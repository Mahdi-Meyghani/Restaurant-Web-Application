from django.urls import path
from . import views


urlpatterns = [
    path('', views.MenuList.as_view(), name='home'),
    path('detail<int:pk>/', views.MenuDetail.as_view(), name='meal_detail'),
    path('about/', views.About.as_view(), name='about')
]