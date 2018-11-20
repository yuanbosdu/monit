from django.contrib import admin
from .models import Zigbee, ZigbeeState, ZigbeeAction
# Register your models here.


class ZigbeeAdmin(admin.ModelAdmin):
    pass


class ZigbeeStateAdmin(admin.ModelAdmin):
    pass


class ZigbeeActionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Zigbee, ZigbeeAdmin)
admin.site.register(ZigbeeState, ZigbeeStateAdmin)
admin.site.register(ZigbeeAction, ZigbeeActionAdmin)
