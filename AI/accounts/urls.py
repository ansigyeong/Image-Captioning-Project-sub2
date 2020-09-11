from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('point/reward/', views.point_reward),
    path('point/use/', views.point_use),
    path('point/<int:user_pk>/', views.point_list),
]