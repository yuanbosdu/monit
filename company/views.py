from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import request, response
# Create your views here.
from django.http.response import JsonResponse
from .models import Device
from zigbee.models import Zigbee


@login_required
@csrf_exempt
def device_list_view(request):
    if request.method == 'POST':
        method = request.POST.get('method', 'delete')
        if method == 'delete':
            device_id = request.POST.get('id')
            print(device_id)
            mdevice = Device.objects.get(id=device_id)
            uuid = mdevice.dtype_uuid
            if mdevice.dprotocol == 'zigbee':
                mzigbee = Zigbee.objects.filter(uuid=uuid).delete()
            mdevice.delete()
        return JsonResponse(dict(msg='OK'))
    context = dict()
    devicelist = Device.objects.all()
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
        
        print(name, description, dtype, dprotocol)
        
        if name is None or name == '' or description is None or  description == '' or dtype is None or dtype == '' or dprotocol is None or dprotocol == '':
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