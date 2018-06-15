from .models import Wallet
import random
import string


# 创建钱包
def create_wallet(user):
    wallet = Wallet()
    wallet.user = user
    wallet.address = get_random_str()
    wallet.save()
    return wallet


# 生成随机钱包地址
def get_random_str():
    return ''.join(random.sample(string.ascii_uppercase + string.ascii_lowercase + string.digits, 15))
