from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse, HttpResponseBadRequest

from api.tool import get_error_json, get_data_json
from .models import Wallet
from .forms import TransferForm, ExtractForm


# 钱包转账
class TransferView(View):
    def patch(self, request):
        transfer_form = TransferForm(request.PATCH)
        if not transfer_form.is_valid():
            return HttpResponseBadRequest(get_error_json(transfer_form), content_type='application/json')
        send_wallet = Wallet.objects.get(user=request.user)     # 转出钱包,当前登录用户的钱包
        receive_address = request.PATCH.get('receive', '')
        receives = Wallet.objects.filter(address=receive_address)
        if not receives:    # 如果接收钱包不存在
            return HttpResponseBadRequest('{"status":"error", "error":1001, "msg":"钱包填写错误"}',
                                          content_type='application/json')
        receive_wallet = receives[0]    # 接收钱包
        num = request.PATCH.get('num', '')
        if send_wallet.money < float(num) or float(num) <= 0:
            return HttpResponseBadRequest('{"status":"error", "error":1003, "msg":"转账不能为负数或者钱包余额不足"}',
                                          content_type='application/json')
        send_wallet.money -= float(num)
        send_wallet.save()
        receive_wallet.money += float(num)
        receive_wallet.save()
        return HttpResponse('{"status": "success"}', content_type='application/json')


# 钱包提取到交易所
class ExtractView(View):
    def patch(self, request):
        extract_form = ExtractForm(request.PATCH)
        if not extract_form.is_valid():
            return HttpResponseBadRequest(get_error_json(extract_form), content_type='application/json')
        wallet = Wallet.objects.get(user=request.user)
        num = request.PATCH.get('num', '')
        if wallet.money < float(num) or float(num) <= 0:
            return HttpResponseBadRequest('{"status":"error", "error":1003, "msg":"提取不能为负数或者钱包余额不足"}',
                                          content_type='application/json')
        wallet.money -= float(num)
        wallet.save()
        return HttpResponse('{"status": "success"}', content_type='application/json')


# 获取当前登录用户的钱包信息
class GetLoginView(View):
    def get(self, request):
        # noinspection PyBroadException
        try:
            mining = Wallet.objects.filter(user=request.user)
            return HttpResponse(get_data_json(mining), content_type='application/json')
        except Exception:
            return HttpResponseBadRequest('{"status":"error", "error":1001, "msg":"没有登录用户"}',
                                          content_type='application/json')
