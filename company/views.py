from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import request, response
# Create your views here.
from django.http.response import JsonResponse
from .models import Device
from zigbee.models import Zigbee


@login_required
def device_list_view(request):
    context = dict()
    devicelist = list()
    for n in range(100):
        devicelist.append(n)
    context.update(devicelist=devicelist)

    return render(request, 'user/devicelist.html', context=context)


@login_required
@csrf_exempt
def device_add_view(request):
    if request.method == 'POST':

        name = request.POST.get('name', None)
        description = request.POST.get('description', None)
        dtype = request.POST.get('dtype', None)
        dprotocol = request.POST.get('dprotocol', None)

        if name is None or description is None or dtype is None or dprotocol is None:
            return JsonResponse(dict(err='input the data'))

        # print(name, description, dtype, dprotocol)
        mdevice = Device.objects.create(name=name, description=description, dtype=dtype, dprotocol=dprotocol)

        if dprotocol == 'zigbee':
            mZigbee = Zigbee.objects.create(name=name, ename=dtype)
            mdevice.dtype_uuid = mZigbee.uuid
            mdevice.save()
            return JsonResponse(dict(err='None'))

    return render(request, 'user/deviceadd.html')


@login_required
def keymaster_view(request):

    return render(request, 'user/keymaster.html')


@login_required
def userlist_view(request):

    return render(request, 'user/userlist.html')


@login_required
def useradd_view(request):

    return render(request, 'user/useradd.html')


@login_required
def user_resetpwd_view(request):

    return render(request, 'user/resetpwd.html')


@login_required
def user_permission_view(request):

    return render(request, 'user/permission.html')