from django.shortcuts import render, get_object_or_404
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
