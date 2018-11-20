from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import request, response
# Create your views here.


@login_required
def device_list_view(request):
    pass

    return render(request, 'user/devicelist.html')


@login_required
def device_add_view(request):

    return render(request, 'user/deviceadd.html')
