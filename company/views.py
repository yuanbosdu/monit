from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import request, response
# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from django.http.response import JsonResponse
from .models import Company, Device, DeviceRuler, SecretKey
from zigbee.models import Zigbee
import random
import datetime
import json
import string
import rsa
from zigbee.models import Zigbee, ZigbeeState
from monit.utils import check_owner, add_company


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
    if len(devicelist) == 0:
        context.update(len=0)
    else:
        context.update(len=devicelist)

    return render(request, 'user/devicelist.html', context=context)


@login_required
@csrf_exempt
@add_company
def device_add_view(request, company=None):
    if request.method == 'POST':

        name = request.POST.get('name', None)
        description = request.POST.get('description', None)
        dtype = request.POST.get('dtype', None)
        dprotocol = request.POST.get('dprotocol', None)
        
        print(name, description, dtype, dprotocol)
        
        if name is None or name == '' or description is None or  description == '' or dtype is None or dtype == '' or dprotocol is None or dprotocol == '':
            return JsonResponse(dict(err='input the data'))

        # print(name, description, dtype, dprotocol)
        mdevice = Device.objects.create(name=name, description=description, dtype=dtype, dprotocol=dprotocol, company=company)

        if dprotocol == 'zigbee':
            mZigbee = Zigbee.objects.create(name=name, ename=dtype)
            mdevice.dtype_uuid = mZigbee.uuid
            mdevice.save()
            return JsonResponse(dict(err='None'))

    return render(request, 'user/deviceadd.html')


@login_required
@add_company
def device_ruler_view(request, company=None):
    # print(company)
    if request.method == 'POST':
        act = request.POST.get('act', None)
        if act is None:
            return JsonResponse(dict(
                err='chose act'
            ))
        if act == 'add':
            name = request.POST.get('name', None)
            description = request.POST.get('description', None)
            ruler = request.POST.get('ruler', None)
            if name is None or description is None or ruler is None:
                return JsonResponse(dict(
                    err='input values'
                ))
            mRuler = DeviceRuler.objects.filter(name=name)
            if len(mRuler) != 0:
                return JsonResponse(dict(
                    err='change the name'
                ))
            else:
                mRuler = DeviceRuler.objects.create(name=name, description=description, ruler=ruler, company=company)
                return JsonResponse(dict(
                    err='None'
                ))
        elif act == 'delete':
            id = request.POST.get('id', None)
            if id is None:
                return JsonResponse(dict(
                    err='None'
                ))
            ret = DeviceRuler.objects.filter(id=id).delete()
            return JsonResponse(dict(
                err='None'
            ))
        return JsonResponse(dict(
            err='None'
        ))
    else:
        rulers = DeviceRuler.objects.filter(company=company)
        context = dict()
        context.update(rulers=rulers)
        return render(request, 'user/deviceruler.html', context=context)


def generator(mCompany):
    mAes = ''.join(random.sample(string.ascii_letters, 16))
    print(mAes)
    (mPub, mPri) = rsa.newkeys(128)
    mSecretKey = SecretKey.objects.create(
        AES=mAes,
        RSA_Public=mPub,
        RSA_Private=mPri,
        company=mCompany)
    return mSecretKey


@login_required
def keymaster_view(request):
    if request.method == 'GET':
        mUser = request.user
        mCompany = Company.objects.filter(admin__username=mUser)[0]
        mSecretKey = SecretKey.objects.filter(company=mCompany)
        if mCompany is not None and len(mSecretKey) is 0:
            mSecretKey = generator(mCompany)
            context = dict(
                sk=mSecretKey
            )
        else:
            context = dict(
                sk=mSecretKey[0]
            )
        return render(request, 'user/keymaster.html', context=context)
    else:
        mReset = request.POST.get('reset', False)
        if mReset is not False:
            mUser = request.user
            mCompany = Company.objects.filter(admin__username=mUser)[0]
            mSecretKey = SecretKey.objects.filter(company=mCompany).delete()
            return JsonResponse(dict(ret='ok'))


@login_required
@check_owner('device')
@add_company
def device_data_view(request, company=None):
    # print(company)
    if request.method == 'POST':
        id = request.POST.get('id', None)
        ruler = request.POST.get('ruler', None)
        # print(id, ruler)
        if id is None or ruler is None:
            return JsonResponse(dict(
                err='chose the ruler'
            ))
        tempDevice = Device.objects.filter(id=id)
        if tempDevice.count() == 0:
            return JsonResponse(dict(err='No Device'))
        tempDevice = tempDevice[0]
        if ruler == '-':
            tempDevice.rulers.set([])
            tempDevice.save()
        else:
            tempDevice.rulers.set([])
            tempDeviceRuler = DeviceRuler.objects.get(name=ruler)
            tempDevice.rulers.add(tempDeviceRuler)
            tempDevice.save()
        return JsonResponse(dict(
            err='None'
        ))
    # check whether the user has the authority

    deviceId = request.GET.get('id')
    mDevice = Device.objects.get(id=deviceId)
    mDeviceRuler = mDevice.rulers.all()
    if mDeviceRuler.count() != 0:
        mDeviceRuler = mDeviceRuler[mDeviceRuler.count()-1]
    else:
        mDeviceRuler = None
    print("*" * 10)
    print(mDeviceRuler)
    print("*" * 10)
    print(mDevice.rulers)
    mRulers = DeviceRuler.objects.filter(company=company)
    print(mDevice.dtype_uuid, mDevice.dtype)

    if mDevice.dprotocol == 'zigbee':
        uuid = mDevice.dtype_uuid
        mZigbeeState = ZigbeeState.objects.filter(zigbee__uuid=uuid).order_by('-utime')[0:10]
    else:
        mZigbeeState = None
    if mZigbeeState is not None:
        statelist = []
        stateticks = []
        i = 1
        for mZS in mZigbeeState:
            statelist.append([i, int(mZS.state)])
            stateticks.append([i, datetime.datetime.strftime(mZS.utime, "%H:%M:%S")])
            i = i + 1
    else:
        statelist = []
        stateticks = []
    # convert statelist to json
    statelist = json.dumps(statelist)
    stateticks = json.dumps(stateticks)

    tempState = []
    if mDeviceRuler is not None and mZigbeeState.count() != 0:
        ruler_str = "%s%s"
        for stat in mZigbeeState:
            temp_ruler_str = ruler_str % (stat.state, mDeviceRuler.ruler)
            ret = eval(temp_ruler_str)
            tempState.insert(-1, dict(
                utime=stat.utime,
                state=stat.state,
                alert=ret
            ))

    if len(tempState) == 0:
        tempState = mZigbeeState
    context = dict(
        Device=mDevice,
        State=tempState,
        Rulers=mRulers,
        CurrentRuler=mDeviceRuler,
        statelist=statelist,
        stateticks=stateticks
    )
    return render(request, 'user/devicedata.html', context=context)


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