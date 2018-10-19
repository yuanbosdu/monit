from django.shortcuts import render

# Create your views here.

from django.http import request, response
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from zigbee.models import Zigbee, ZigbeeState

device_list = [
    'Gas',
    'Alcohol',
    'Hall',
    'Shock',
    'Pir',
    'Humidity:',
]

device_name = [
    '气体监测',
    '酒精监测',
    'Hall监测',
    'Shock监测',
    'Pir监测'
    '温湿度监测',
]

@csrf_exempt
def serial_push(request):
    zigbee_name = request.POST.get("name")
    zigbee_english = request.POST.get('english')
    print(zigbee_name)
    print(zigbee_english)
    zigbee_state = request.POST.get("state")
    print(zigbee_state)

    if zigbee_english not in device_list:
        print("Unexpect device name")
        return  HttpResponse('Unexpect device')

    #first get the object
    ob = Zigbee.objects.filter(english=zigbee_english)
    print(ob)
    print(len(ob))
    if len(ob) != 0:
        print(ob[0])
        print(ob[0].state.all())

        # insert the new state info to the database
        # check the text must be in "Normal!" or "Alarm!"
        if zigbee_english != 'Humidity:' and zigbee_state in ['Normal!', 'Alarm!']:
            mZigbee_state = ZigbeeState.objects.create(zigbee=ob[0], state=zigbee_state)
        if zigbee_english == 'Humidity:':
            mZigbee_state = ZigbeeState.objects.create(zigbee=ob[0], state=zigbee_state)

    else:
        # create the new object
        mZigbee = Zigbee.objects.create(english=zigbee_english, name=zigbee_name)
        # insert the new state info to the database
        # check the text must be in "Normal!" or "Alarm!"
        if zigbee_english != 'Humidity:' and zigbee_state in ['Normal!', 'Alarm!']:
            mZigbee_state = ZigbeeState.objects.create(zigbee=mZigbee, state=zigbee_state)
        if zigbee_english == 'Humidity:':
            mZigbee_state = ZigbeeState.objects.create(zigbee=mZigbee, state=zigbee_state)
        print('add the new record in the database')
    return HttpResponse('OK')

