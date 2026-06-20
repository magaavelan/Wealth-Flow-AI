from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_home, name='dashboard_home'),
    path('chat/new/', views.create_new_session, name='create_new_session'),
    path('chat/<int:session_id>/', views.chat_session_detail, name='chat_session_detail'),
    path('chat/<int:session_id>/send/', views.send_message_api, name='send_message_api'),
]