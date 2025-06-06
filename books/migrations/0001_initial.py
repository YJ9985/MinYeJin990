# Generated by Django 4.2.5 on 2025-04-18 06:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('customer_review_rank', models.IntegerField()),
                ('author', models.CharField(max_length=15)),
                ('author_profile_img', models.ImageField(blank=True, upload_to='author_profiles/')),
                ('author_info', models.TextField(blank=True)),
                ('author_works', models.CharField(blank=True, max_length=50)),
                ('cover_image', models.ImageField(blank=True, upload_to='book_covers/')),
                ('audio_file', models.FileField(blank=True, null=True, upload_to='tts/')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('LITERATURE', '소설/시/희곡'), ('ECONOMY', '경제/경영'), ('DEVELOPMENT', '자기계발'), ('HUMANITY', '인문/교양'), ('SCIENCE', '과학'), ('HOBBY', '취미/실용'), ('MINORS', '어린이/청소년')], help_text='도서 종류를 선택해주세요.', max_length=100, unique=True, verbose_name='카테고리')),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('reading_date', models.DateField(blank=True, null=True)),
                ('cover_img', models.ImageField(blank=True, null=True, upload_to='thread_covers/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book', verbose_name='해당 도서')),
                ('like_users', models.ManyToManyField(blank=True, related_name='liked_threads', to=settings.AUTH_USER_MODEL, verbose_name='좋아요한 사용자')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.category'),
        ),
        migrations.AddField(
            model_name='book',
            name='users',
            field=models.ManyToManyField(related_name='books', to=settings.AUTH_USER_MODEL, verbose_name='등록한 사용자'),
        ),
    ]
