# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
import MySQLdb
from ujourney.models import Users
from django.contrib import auth

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # ���������� ������ � ������������ "�������"
        auth.login(request, user)
        # ��������������� �� "����������" ��������
        return HttpResponseRedirect("/account/loggedin/")
    else:
        # ����������� �������� � �������
        return render_to_response("registration/login.html")

def logout(request):
    auth.logout(request)
    # ��������������� �� ��������.
    return HttpResponseRedirect("/account/loggedout/")
	
def my_view(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/?next=%s' % request.path)

