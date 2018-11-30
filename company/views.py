from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import request, response
# Create your views here.


@login_required
def device_list_view(request):
    context = dict()
    devicelist = list()
    for n in range(100):
        devicelist.append(n)
    context.update(devicelist=devicelist)

    return render(request, 'user/devicelist.html', context=context)


@login_required
def device_add_view(request):

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