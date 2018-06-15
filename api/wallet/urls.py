import django
from django.urls import path
from wallet.views import TransferView, ExtractView, GetLoginView

app_name = "wallet"

urlpatterns = [
    path('transfer/', TransferView.as_view(), name="wallet_transfer"),
    path('extract/', ExtractView.as_view(), name="wallet_extract"),
    path('get/login/', GetLoginView.as_view(), name="wallet_get_login")
]