from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('board/', views.board, name="board"),
    path('board/<int:pk>/', views.board_detail, name='board_detail'),
    path('board/new/', views.board_new, name='board_new'),
]