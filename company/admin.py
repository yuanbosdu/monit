from django.contrib import admin
from .models import Company, Device, SecretKey, UserInfo
# Register your models here.


class CompanyAdmin(admin.ModelAdmin):
    pass


class DeviceAdmin(admin.ModelAdmin):
    pass


class SecretKeyAdmin(admin.ModelAdmin):
    pass


class UserInfoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Company, CompanyAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(SecretKey, SecretKeyAdmin)
admin.site.register(UserInfo, UserInfoAdmin)

