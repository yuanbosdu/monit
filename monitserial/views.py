from django.shortcuts import render

# Create your views here.

from django.http import request, response
from django.shortcuts import render_to_response
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from zigbee.models import Zigbee, ZigbeeState, ZigbeeAction

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

@csrf_exempt
def serial_push(request):
    zigbee_name = request.POST.get("name")
    zigbee_ename = request.POST.get('ename')
    print("serial push logs")
    print(zigbee_name)
    print(zigbee_ename)
    zigbee_state = request.POST.get("state")
    print(zigbee_state)

    if zigbee_ename not in device_list:
        print("Unexpect device name")
        return  HttpResponse('Unexpect device')

    #first get the object
    ob = Zigbee.objects.filter(ename=zigbee_ename)
    print(ob)
    print(len(ob))
    if len(ob) != 0:
        print(ob[0])
        print(ob[0].state.all())

        # insert the new state info to the database
        # check the text must be in "Normal!" or "Alarm!"
        if zigbee_ename != 'Humidity:' and zigbee_state in ['Normal!', 'Alarm!', 'ON', 'OFF']:
            mZigbee_state = ZigbeeState.objects.create(zigbee=ob[0], state=zigbee_state)
        if zigbee_ename == 'Humidity:':
            mZigbee_state = ZigbeeState.objects.create(zigbee=ob[0], state=zigbee_state)

    else:
        # create the new object
        mZigbee = Zigbee.objects.create(ename=zigbee_ename, name=zigbee_name)
        # insert the new state info to the database
        # check the text must be in "Normal!" or "Alarm!"
        if zigbee_ename != 'Humidity:':  # and zigbee_state in ['Normal!', 'Alarm!']:
            mZigbee_state = ZigbeeState.objects.create(zigbee=mZigbee, state=zigbee_state)
        if zigbee_ename == 'Humidity:':
            mZigbee_state = ZigbeeState.objects.create(zigbee=mZigbee, state=zigbee_state)
        print('add the new record in the database')
    return HttpResponse('OK')


from rabbitmq.views import mq_push
import json
@csrf_exempt
def serial_change(request):
    mZigbeeName = request.POST.get('name', None)
    mZigbeeEname = request.POST.get('ename', None)
    mZigbeeAction = request.POST.get('action', None)
    mZigbeeNewState = request.POST.get('newstate', None)

    print(mZigbeeEname)

    if mZigbeeEname is None or mZigbeeAction is None or mZigbeeNewState is None:
        return JsonResponse({
            'err': 'please input the data',
        })

    # first find the zigbee
    mZigbee = Zigbee.objects.filter(ename=mZigbeeEname)
    if len(mZigbee) == 0:
        return  JsonResponse({
            'err': 'there is no zigbee'
        })
    else:
        mZigbee = mZigbee[0]
    # get the latest zigbee state
    mZigbeeState = ZigbeeState.objects.filter(zigbee=mZigbee).order_by('-utime')[0]

    # create the newaction
    mNewState = ZigbeeAction.objects.create(zigbee=mZigbee, zigbee_state=mZigbeeState, action=mZigbeeAction,
                                            newstate=mZigbeeNewState)

    # push the new job to the rabbitmq
    body = dict()
    body['ename'] = mZigbeeEname
    body['newstate'] = mZigbeeNewState

    mq_push(json.dumps(body))

    return JsonResponse({
        'err': 'None',
        'message': 'OK',
    })

@csrf_exempt
def serial_get(request):
    # get the action
    # for debug, we only get the change of 'taideng'
    mZigbeeAction = ZigbeeAction.objects.filter(zigbee__ename='Taideng').order_by('-ctime')
    mZigbeeState = ZigbeeState.objects.filter(zigbee__ename='Taideng').order_by('-utime')

    # print(mZigbeeAction)
    if len(mZigbeeAction) == 0 or len(mZigbeeState) == 0:
        return JsonResponse({
            'err': 'there is no action or state need change',
        })
    else:
        # print(mZigbeeAction)
        mZigbeeAction = mZigbeeAction[0]
        mZigbeeState = mZigbeeState[0]
        if mZigbeeAction.done is True:  # or (mZigbeeState.state == mZigbeeAction.newstate):
            return JsonResponse({
                'err': 'there is no action need change',
            })
        else:
            return JsonResponse({
                'err': 'None',
                'english': mZigbeeAction.zigbee.ename,
                'newstate': mZigbeeAction.newstate,
            })



