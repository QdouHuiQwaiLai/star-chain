from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse, HttpResponseBadRequest
from api.tool import get_error_json, get_data_json
import json
from datetime import datetime
import time
from .models import Mining
from .forms import PromoteForm
from HOST import HOST


# Create your views here.
# 得到算力排行榜TOP10
class RankView(View):
    def get(self, request):
        rank_list = Mining.objects.order_by('-force')[0:10]     # 以force倒序选取10个
        data = json.loads(get_data_json(rank_list, False))
        for i in range(len(data["data"])):  # 把user名字插入到返回的json
            data["data"][i]["name"] = rank_list[i].user.name
        data_json = json.dumps(data)
        return HttpResponse(data_json, content_type='application/json')


# 提升矿机算力
class PromoteView(View):
    def patch(self, request):
        promote_form = PromoteForm(request.PATCH)
        if not promote_form .is_valid():
            return HttpResponseBadRequest(get_error_json(promote_form), content_type='application/json')
        num = request.PATCH.get('num', '')
        if int(num) < 0:
            return HttpResponseBadRequest('{"status":"error", "error":1003, "msg":"算力提升不能为负数"}',
                                          content_type='application/json')
        mining = Mining.objects.get(user=request.user)
        mining.force += int(num)
        mining.save()
        return HttpResponse('{"status": "success"}', content_type='application/json')


# 获取当前登录用户的矿机信息
class GetLoginView(View):
    def get(self, request):
        print(request.user)
        # noinspection PyBroadException
        try:
            mining = Mining.objects.filter(user=request.user)
            return HttpResponse(get_data_json(mining), content_type='application/json')
        except Exception:
            return HttpResponseBadRequest('{"status":"error", "error":1001, "msg":"没有登录用户"}',
                                          content_type='application/json')


# 领取矿石到钱包
class GainView(View):
    def patch(self, request):
        mining = Mining.objects.get(user=request.user)
        mining_time = datetime.strptime(mining.add_time.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
        now_time = datetime.strptime(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
        total = int((now_time - mining_time).seconds / 30)  # 矿机产矿石总量
        num = request.PATCH.get('num', '')  # 需要提取的矿石
        if total < (mining.extract + float(num)):
            return HttpResponseBadRequest('{"status":"error", "error":1003, "msg":"矿石余额不足"}',
                                          content_type='application/json')
        mining.extract += float(num)
        mining.save()
        mining.wallet.money += float(num)
        mining.wallet.save()
        return HttpResponse('{"status": "success"}', content_type='application/json')


# 获取当前矿机的可领取矿石
class GetMayView(View):
    def get(self, request):
        mining = Mining.objects.get(user=request.user)
        mining_time = datetime.strptime(mining.add_time.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
        now_time = datetime.strptime(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
        total = int((now_time - mining_time).seconds / 30)  # 矿机产矿石总量
        may_num = total - mining.extract
        data = {"status": "success", "data": {}}
        data["data"]["may_num"] = may_num
        return HttpResponse(json.dumps(data), content_type='application/json')


# 矿机签到处理
class SignView(View):
    def get(self, request):
        mining = Mining.objects.get(user=request.user)
        data = {"status": "success", "data": {}}
        if not mining.sign_time:    # 如果没有签过到返回真
            data["data"]["signed"] = False
            return HttpResponse(json.dumps(data), content_type='application/json')
        today_time = datetime.strptime(datetime.now().strftime('%Y-%m-%d'), '%Y-%m-%d')
        sign_time = datetime.strptime(mining.sign_time.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
        if today_time > sign_time:  # 如果签到时间小于今天返回真
            data["data"]["signed"] = False
            return HttpResponse(json.dumps(data), content_type='application/json')
        data["data"]["signed"] = True
        return HttpResponse(json.dumps(data), content_type='application/json')

    def patch(self, request):
        mining = Mining.objects.get(user=request.user)
        mining.sign_time = datetime.now()
        mining.save()
        return HttpResponse('{"status": "success"}', content_type='application/json')


