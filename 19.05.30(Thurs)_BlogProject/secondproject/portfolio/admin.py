from django.contrib import admin

from .models import Portfolio

# Register your models here.

# django admin에게 새로운 모델이 생겼다고 알려주는 것
admin.site.register(Portfolio)



