from django.contrib import admin
from .models import Mining


# Register your models here.
class MiningAdmin(admin.ModelAdmin):
    list_display = ('user', 'wallet', 'force', 'add_time', 'extract')


admin.site.register(Mining, MiningAdmin)
