from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
    path('profile/<int:user_pk>/',views.profile,name='profile'),
    path('profile/<int:user_pk>/follow/', views.follow, name='follow'),
]
