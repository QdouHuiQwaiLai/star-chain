import django
from django.urls import path
from mining.views import RankView, PromoteView, GetLoginView, GainView, GetMayView, SignView

app_name = "mining"

urlpatterns = [
    path('rank/', RankView.as_view(), name="mining_rank"),
    path('promote/', PromoteView.as_view(), name="mining_promote"),
    path('get/login/', GetLoginView.as_view(), name="mining_get_login"),
    path('gain/', GainView.as_view(), name="mining_gain"),
    path('get/may/', GetMayView.as_view(), name="mining_get_view"),
    path('sign/', SignView.as_view(), name="mining_sign"),
]