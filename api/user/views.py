from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
# 进行密码加密
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, HttpResponseBadRequest
from .models import UserProfile
from .forms import RegisterForm, LoginForm
from api.tool import get_error_json, get_data_json
import json
import time
from wallet.create_wallet import create_wallet
from mining.create_mining import create_mining
import simplejson
# Create your views here.


# 用户注册
class RegisterView(View):
    def post(self, request):
        register_form = RegisterForm(request.POST)
        if not register_form.is_valid():    # 不通过验证
            return HttpResponseBadRequest(get_error_json(register_form), content_type='application/json')
        user_name = request.POST.get("username", "")
        if UserProfile.objects.filter(username=user_name):  # 此用户已经存在
            return HttpResponseBadRequest('{"status":"error", "error":1002, "msg":"此用户已经存在"}',
                                          content_type='application/json')
        email = request.POST.get("email", "")
        pass_word = request.POST.get("password", "")
        name = request.POST.get("name", "")
        user_profile = UserProfile()
        user_profile.username = user_name
        user_profile.email = email
        user_profile.password = make_password(pass_word)
        user_profile.name = name
        user_profile.save()
        wallet = create_wallet(user_profile)
        create_mining(user_profile, wallet)
        return HttpResponse('{"status":"success"}', content_type='application/json')


# 用户登录
class LoginView(View):
    def post(self, request):
        login_form = LoginForm(request.POST)
        if not login_form.is_valid():
            return HttpResponseBadRequest(get_error_json(login_form), content_type='application/json')

        user_name = request.POST.get("username", "")
        pass_word = request.POST.get("password", "")

        # 成功返回user对象,失败返回null
        user = authenticate(username=user_name, password=pass_word)
        if user is None:
            return HttpResponseBadRequest('{"status":"error", "error":1003, "msg":"用户名或者密码错误"}',
                                          content_type='application/json')
        login(request, user)
        return HttpResponse('{"status":"success"}', content_type='application/json')


# 退出登录状态
class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponse('{"status":"success"}', content_type='application/json')


# 获取当前登录用户的信息
class GetLoginUserView(View):
    def get(self, request):
        # noinspection PyBroadException
        try:
            user = UserProfile.objects.get(username=request.user)
            data_json = {"status": "success", "data": {}}
            data_json['data']['username'] = user.username
            data_json['data']['email'] = user.email
            return HttpResponse(json.dumps(data_json), content_type='application/json')
        except Exception:
            return HttpResponseBadRequest('{"status":"error", "error":1001, "msg":"没有登录用户"}',
                                          content_type='application/json')


