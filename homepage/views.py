from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from zigbee.models import Zigbee, ZigbeeState
from datetime import datetime
import time

# Create your views here.

from homepage.tasks import mul

device_list = [
    'Gas',
    'Alcohol',
    'Hall',
    'Shock',
    'Pir',
    'Humidity:',
    'Taideng',
]

device_name = [
    '气体监测',
    '酒精监测',
    'Hall监测',
    'Shock监测',
    'Pir监测'
    '温湿度监测',
    '台灯',
]


def index(request):
    gas_device = Zigbee.objects.filter(english='Gas')
    if len(gas_device) == 0:
        context = {
            'gas_state': [],
        }
        return render(request, "index.html", context=context)
    gas_device = gas_device[0]
    context = {
        'gas_state': [],
    }
    if gas_device is not None:
        gas_state = gas_device.state.all().order_by('-utime')
        print(gas_state)
        for gs in gas_state:
            context['gas_state'].append((gs.utime.strftime('%m/%d %H:%M:%S'), gs.state))
        print(context)

    return render(request, "index.html", context=context)


@csrf_exempt
def api_device(request):
    if request.method == 'GET':
        device_english = request.GET.get('english', None)
        if device_english is None:
            return JsonResponse({
                'code': 'Unexpect device',
            })
        zigbee_devices = Zigbee.objects.filter(english=device_english)
        if len(zigbee_devices) == 0:
            return JsonResponse({
                'code': 'No record',
            })
        zigbee_device = zigbee_devices[0]
        # we only get the latest 10 records
        zigbee_state = zigbee_device.state.all().order_by('-utime')[:10]
        # print(zigbee_state)
        ret = []
        for zs in zigbee_state:
            ret.append((zs.utime.strftime('%m/%d %H:%M:%S'), zs.state))
        return JsonResponse(ret, safe=False)

