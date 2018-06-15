from django.contrib import admin
from .models import Wallet
# Register your models here


class WalletAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'money')


admin.site.register(Wallet, WalletAdmin)
