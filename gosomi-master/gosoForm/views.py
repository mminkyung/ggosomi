from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.utils import timezone
from .models import Photo
from .forms import UploadForm
from django.views.generic.list import ListView
from django.contrib.auth.models import User

# Create your views here.
def upload(request):
       
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES) # 대용량인 이미지를 처리해야 하므로 두 매개변수를 넘겨줘야함.
        if form.is_valid():
            photo = form.save(commit=False) # photo객체를 가져오긴 하나 DB에 아직 저장하진 않음
            photo.owner = request.user      # request.user는 로그인한 사용자
            form.save()
            return render(request, 'home.html', {'form' : form})
            # return redirect(home)
    else:
        form = UploadForm()
    return render(request, 'upload.html', {'form' : form})

class HomeView(ListView):
    # model = Photo 이렇게 해주면 사용자를 안가리고 모든 photo객체가 넘어가게 되므로 아래와 같이 쿼리를 지정해줌.
    context_object_name = 'user_photo_list' # 템플릿에 전달되는 이름

    def get_queryset(self):
        user = self.request.user    # 로그인되어있는 사용자
        return user.photo_set.all().order_by('pub_date')