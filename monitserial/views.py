from django.shortcuts import render

# Create your views here.

from django.http import request, response
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from zigbee.models import Zigbee, ZigbeeState


@csrf_exempt
def serial_push(request):
    zigbee_name = request.POST.get("name")
    print(zigbee_name)
    zigbee_state = request.POST.get("state")
    print(zigbee_state)

    #first get the object
    ob = Zigbee.objects.filter(name=zigbee_name)
    print(ob)
    print(ob[0])
    print(ob[0].state)

    state = ZigbeeState.objects.filter(zigbee=ob[0])
    print(state)

    return HttpResponse('OK')
