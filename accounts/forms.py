from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from books.models import Category

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    # 관심 장르: Category에서 가져옴
    interested_genres = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="관심 장르"
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'username',
            'last_name',
            'first_name',
            'email',
            'gender',
            'age',
            'weekly_reading_time',
            'yearly_reading_count',
            'profile_image',
            'interested_genres',  # 실제 DB에는 favorite_categories로 저장됨
        )
        labels = {
            'username': '아이디',
            'last_name': '성',
            'first_name': '이름',
            'email': '이메일',
            'gender': '성별',
            'age': '나이',
            'weekly_reading_time': '주간 평균 독서 시간',
            'yearly_reading_count': '연간 독서량',
            'profile_image': '프로필 사진',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = "비밀번호"
        self.fields['password2'].label = "비밀번호 확인"

    def save(self, commit=True):
        user = super().save(commit=False)
        # ModelMultipleChoiceField로 받은 queryset을 name 문자열로 변환
        genres = self.cleaned_data.get('interested_genres')
        if genres:
            user.favorite_categories = ','.join([g.name for g in genres])
        if commit:
            user.save()
        return user
    

class CustomUserChangeForm(UserChangeForm):
    # 관심 장르 필드 (체크박스 + 복수 선택)
    interested_genres = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="관심 장르"
    )

    class Meta(UserChangeForm.Meta):
        model = User
        fields = (
            'username',
            'last_name',
            'first_name',
            'email',
            'gender',
            'age',
            'weekly_reading_time',
            'yearly_reading_count',
            'profile_image',
            'interested_genres',
        )
        labels = {
            'username': '아이디',
            'last_name': '성',
            'first_name': '이름',
            'email': '이메일',
            'gender': '성별',
            'age': '나이',
            'weekly_reading_time': '주간 평균 독서 시간',
            'yearly_reading_count': '연간 독서량',
            'profile_image': '프로필 사진',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 초기값 설정: 쉼표로 저장된 문자열을 → Category 객체 리스트로
        if self.instance and self.instance.favorite_categories:
            category_names = self.instance.favorite_categories.split(',')
            self.initial['interested_genres'] = Category.objects.filter(name__in=category_names)

    def save(self, commit=True):
        user = super().save(commit=False)
        genres = self.cleaned_data.get('interested_genres')
        if genres:
            user.favorite_categories = ','.join([g.name for g in genres])
        else:
            user.favorite_categories = ''
        if commit:
            user.save()
        return user