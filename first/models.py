from django.db import models
# db 테이블 구조 = 모델 만들기

# Create your models here.

class Question(models.Model): #질문
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self): #코드 대신 리턴하여 출력
        return self.subject

class Answer(models.Model): #대답
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #연결한다, question을 삭제하면 대답도 삭제한다
    content = models.TextField()
    create_date = models.DateTimeField()
