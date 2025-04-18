# users/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # 성별: 선택지 제공 (M/F)
    GENDER_CHOICES = [
        ('M', '남성'),
        ('F', '여성'),
    ]
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        blank=True,
        null=True,
        verbose_name='성별',
    )

    # 나이 (빈 값 허용)
    age = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name='나이',
    )

    # 주간 평균 독서 시간
    weekly_reading_time = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name='주간 평균 독서 시간 (시간)',
    )

    # 연간 독서량
    yearly_reading_count = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name='연간 독서량 (권)',
    )

    # 프로필 사진
    profile_image = models.ImageField(
        upload_to='profile_images/',
        blank=True,
        null=True,
        verbose_name='프로필 사진',
    )

    # 관심 장르
    favorite_categories = models.CharField(
        max_length=600,
        blank=True,
        verbose_name='관심 장르',
        help_text='선택된 장르를 쉼표(,)로 구분하여 저장합니다.',
    )

    def get_favorite_categories_display(self):
        return self.favorite_categories.split(',') if self.favorite_categories else []

    def __str__(self):
        return self.username
