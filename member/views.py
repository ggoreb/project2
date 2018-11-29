from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from django.utils import timezone

# @csrf_exempt
from member.models import Member

def login(request):
    if request.method == 'GET':
        return render(
            request,
            'member/login.html'
        )
    else:
        id = request.POST['id']
        pw = request.POST['pw']

        m = Member.objects.get(
            user_id=id, user_pw=pw)
        return HttpResponse(
            m.user_id + '님 반갑습니다.')

def join(request):
    print(request.method)
    if request.method == 'GET':
        return render(
            request,
            'member/join.html'
        )
    else:
        id = request.POST['id']
        pw = request.POST['pw']
        name = request.POST['name']

        m = Member(
            user_id=id, user_pw=pw,
            user_name=name,
            c_date=timezone.now())
        m.save()

    return HttpResponse(id+pw+name)









