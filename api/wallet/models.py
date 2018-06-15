from django.db import models
from user.models import UserProfile


# Create your models here.
class Wallet(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u"所属用户")
    address = models.CharField(max_length=100, verbose_name=u"钱包地址")
    money = models.FloatField(default=0.0, verbose_name=u"钱包余额")

    class Meta:
        verbose_name = u'钱包信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}'.format(self.address)
