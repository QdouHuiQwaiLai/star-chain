from .models import Mining


def create_mining(user, wallet):
    mining = Mining()
    mining.user = user
    mining.wallet = wallet
    mining.save()
