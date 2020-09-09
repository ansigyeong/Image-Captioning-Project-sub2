from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('notice/', views.notice_list),
    path('notice/create/', views.notice_create),
    path('notice/<int:notice_pk>', views.notice_detail),

]