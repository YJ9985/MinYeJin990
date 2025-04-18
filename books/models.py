from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    customer_review_rank = models.IntegerField()
    author = models.CharField(max_length=15)
    author_profile_img = models.ImageField(upload_to="author_profiles/", blank=True)
    author_info = models.TextField()
    author_works = models.CharField(max_length=50)
    cover_image = models.ImageField(blank=True)
    audio_file = models.FileField(upload_to="tts/", blank=True, null=True)
    CATEGORY_CHOICES = [
        ('LITERATURE', '소설/시/희곡'),
        ('ECONOMY', '경제/경영'),
        ('DEVELOPMENT', '자기계발'),
        ('HUMANITY', '인문/교양'),
        ('SCIENCE', '과학'),
        ('HOBBY', '취미/실용'),
        ('MINORS', '어린이/청소년'),
    ]

    category = models.CharField(
        max_length=100,
        unique=True,
        choices=CATEGORY_CHOICES,
        help_text = '도서 종류를 선택해주세요.',
        verbose_name='종류',
        )

class Category(models.Model):
    CATEGORY_CHOICES = [
        ('LITERATURE', '소설/시/희곡'),
        ('ECONOMY', '경제/경영'),
        ('DEVELOPMENT', '자기계발'),
        ('HUMANITY', '인문/교양'),
        ('SCIENCE', '과학'),
        ('HOBBY', '취미/실용'),
        ('MINORS', '어린이/청소년'),
    ]

    name = models.CharField(
        max_length=100,
        unique=True,
        choices=CATEGORY_CHOICES,
        help_text = '도서 종류를 선택해주세요.',
        verbose_name='종류',
        )

    def __str__(self):
        return self.name
    
# 특정 도서에 대한 게시글
# class Thread(models.Model):
    title = models.ForeignKey(Book, on_delete=models.CASCADE)