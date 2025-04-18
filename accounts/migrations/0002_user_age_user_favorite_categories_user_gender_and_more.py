# Generated by Django 4.2.5 on 2025-04-11 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='나이'),
        ),
        migrations.AddField(
            model_name='user',
            name='favorite_categories',
            field=models.CharField(blank=True, help_text='선택된 장르를 쉼표(,)로 구분하여 저장합니다.', max_length=600, verbose_name='관심 장르'),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', '남성'), ('F', '여성')], max_length=1, null=True, verbose_name='성별'),
        ),
        migrations.AddField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images/', verbose_name='프로필 사진'),
        ),
        migrations.AddField(
            model_name='user',
            name='weekly_reading_time',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='주간 평균 독서 시간 (시간)'),
        ),
        migrations.AddField(
            model_name='user',
            name='yearly_reading_count',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='연간 독서량 (권)'),
        ),
    ]
