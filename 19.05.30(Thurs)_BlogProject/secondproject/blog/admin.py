from django.contrib import admin
from .models import Blog # 같은 폴더안에 있 model.py에서 정의된 Blog 객체를 불러온다.import

# Register your models here.

# admin 사이트에 객체 Blog를 등록
admin.site.register(Blog)
