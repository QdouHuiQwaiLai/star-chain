from django.db import models
from user.models import UserProfile
from wallet.models import Wallet
from datetime import datetime


# Create your models here.
class Mining(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u"所属用户")
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, verbose_name=u"所属钱包")
    force = models.IntegerField(default=100, verbose_name=u"矿机算力")
    # 这里要用datetime.now 不能用 datetime.now()
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')
    extract = models.FloatField(default=0, verbose_name=u"已经被取到钱包的矿石")
    sign_time = models.DateTimeField(null=True, blank=True, verbose_name=u"用户签到的时间")

    class Meta:
        verbose_name = u'矿机信息'
        verbose_name_plural = verbose_name

