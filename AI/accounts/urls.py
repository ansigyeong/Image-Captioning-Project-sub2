from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('point/reward/', views.point_reward),
    path('point/<int:user_pk>/', views.point_list),
    path('daily/<int:user_pk>/', views.daily),
]