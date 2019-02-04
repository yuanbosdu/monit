# -*- coding: utf-8 -*-
from functools import wraps
from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from zigbee.models import Zigbee
from company.models import Company, Device


def check_owner(obj):
    def wrap_function(func):
        @wraps(func)
        def return_function(request, *args, **kwargs):
            user = request.user
            if not request.user.is_authenticated:
                return HttpResponseRedirect(reverse('user_login'))
            mCompany = Company.objects.filter(admin__username=user)
            if len(mCompany) == 0:
                return HttpResponseRedirect(reverse('user_index'))
            mCompany = mCompany[0]
            if request.method == 'GET':
                id = request.GET.get('id', None)
            else:
                id = request.POST.get('id', None)
            if id is None:
                return HttpResponseRedirect(reverse('user_index'))
            if obj == 'device':
                mDevice = Device.objects.filter(company=mCompany, id=id)
                # print('mDevice', mDevice)
                if len(mDevice) == 0:
                    return HttpResponseRedirect(reverse('user_index'))
                else:
                    return func(request, *args, **kwargs)
        return return_function
    return wrap_function


def add_company(func):
    @wraps(func)
    def return_function(request, company=None):
        user = request.user
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('user_login'))
        mCompany = Company.objects.filter(admin__username=user)
        if len(mCompany) == 0:
            return HttpResponseRedirect(reverse('user_index'))
        mCompany = mCompany[0]
        return func(request, company=mCompany)
    return return_function

