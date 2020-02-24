from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('board/', views.board, name="board"),
    path('post/<int:post_id>/', views.board_detail, name='board_detail'),
    path('post/new/', views.board_new, name='board_new'),
    path('post/create/', views.board_create, name='board_create'),
]