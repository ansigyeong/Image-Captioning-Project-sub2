from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('notice/', views.notice_list),
    path('notice/create/', views.notice_create),
    path('notice/<int:notice_pk>/', views.notice_detail),
    path('notice/<int:notice_pk>/delete/', views.notice_delete),


    path('suggestion/', views.suggestion_list),
    path('suggestion/create/', views.suggestion_create),
    path('suggestion/<int:suggestion_pk>/', views.suggestion_detail),
    path('suggestion/<int:suggestion_pk>/delete/', views.suggestion_delete),

    
]