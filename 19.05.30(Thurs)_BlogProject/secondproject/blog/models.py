from django.db import models

# Create your models here.

# models라는 의미는 클래스 Blog가 장고 Model임을 알려주는 것, 장고에서 모델은 데이터베이스. 즉 데이터베이스에 저장됨을 알게됨
class Blog(models.Model):
    # models.CharField : 글자수가 제한된 텍스트를 정의할때 사용 -> 글제목에 사용
    title = models.CharField(max_length = 200)
    # models.DateTimeField 날짜와 시간을 의미
    pub_date = models.DateTimeField('date published')
    # 글자수에 제한이 없는 긴 텍스트를 위한 속성
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[ :100]

