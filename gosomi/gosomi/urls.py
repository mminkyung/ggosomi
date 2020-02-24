
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from post import views
import mainpage.views
import gosoForm.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', include('post.urls')),
    path('', mainpage.views.home, name = "home"),
    path('logout/', mainpage.views.logout, name='logout'),
    path('signup/', mainpage.views.signup, name='signup'),
    path('mypage/', mainpage.views.mypage, name = 'mypage'),
    path('signup/checkid/', mainpage.views.checkid, name='checkid'),

    
    # 고소하기 url
    path('upload/', gosoForm.views.upload, name = "upload"),
    path('photo/<int:post_id>', gosoForm.views.detail_post, name = "detail_post"),
    path('mainpage/postpage', gosoForm.views.postpage , name = "postpage"),
    # 인증메일 보내기 url
    path('activate/<str:uid64>/<str:token>/', mainpage.views.activate, name='activate'),

]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
