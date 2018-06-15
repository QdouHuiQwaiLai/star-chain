import django
from django.urls import path
from user.views import RegisterView, LoginView, LogoutView, GetLoginUserView

app_name = "user"

urlpatterns = [
    path('register/', RegisterView.as_view(), name="user_register"),
    path('login/', LoginView.as_view(), name="user_login"),
    path('logout/', LogoutView.as_view(), name="user_logout"),
    path('get/login/', GetLoginUserView.as_view(), name="user_get_login"),
]