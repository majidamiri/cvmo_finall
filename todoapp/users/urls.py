from django.urls import path
from . import views
from .views import UserRegistrationAPIView, UserLoginAPIView, UserTokenAPIView

app_name = 'users'

urlpatterns = [
    path('users/', UserRegistrationAPIView.as_view(), name="list"),
    path('users/resend_code', UserRegistrationAPIView.as_view(), name="resend_code"),
    path('users/verify', UserRegistrationAPIView.as_view(), name="list"),
    path('users/login/', UserLoginAPIView.as_view(), name="login"),
    path('tokens/<key>/', UserTokenAPIView.as_view(), name="token"),
    path('users_registration', views.login_page, name='index'),
    path('profile', views.profile, name='profile'),
    path('users/logout', views.logout, name='logout'),
    path('', views.index, name='index'),
]
