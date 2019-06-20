from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

# Create your views here.

def home(request):
    # queryset : 모델로부터 전달받은 객체 method queryset의 기능을 처리하고 정렬
    blogs = Blog.objects
    # blogs를 사전형 객체 blogs에 담는다. 이는 templates을 출력을 위해한다.
    return render(request, 'home.html', {'blogs': blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'blog': blog_detail})

# new.html을 띄워주는 함수.
def new(request):
    return render(request, 'new.html')

# 입력받은 내용을 데이터베이스에 넣어주는 함수.
def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save() # 쿼리셋 관렴 함수, 데이터 베이스에 넣어라는 명령,
    return redirect('/blog/' +str(blog.id))
