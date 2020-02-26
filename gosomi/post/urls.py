from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('board/', views.board, name="board"),
    path('post/<int:post_id>/', views.board_detail, name='board_detail'),
    path('post/new/', views.board_new, name='board_new'),
    path('post/create/', views.board_create, name='board_create'),
    path('post/<int:post_id>', views.board_delete, name = 'board_delete'),
    path('post/update/<int:post_id>', views.board_update, name = "board_update"),
    path('post/edit/<int:post_id>', views.board_edit, name = "board_edit"),


]