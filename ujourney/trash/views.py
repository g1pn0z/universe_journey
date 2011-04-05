# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
import MySQLdb
from ujourney.models import Users

def level_0(request):
	return render_to_response('index.html')

def post_comment(request, new_comment):
    if request.session.get('has_commented', False):
        return HttpResponse("�� ��� ��������� �����������")
    c = comments.Comment(comment=new_comment)
    c.save()
    request.session['has_commented'] = True
    return HttpResponse('������� �� ��� �����������!')

def login(request):
    try:
        m = Member.objects.get(username__exact=request.POST['username'])
        if m.password == request.POST['password']:
            request.session['member_id'] = m.id
            return HttpResponse("�� ������������.")
    except Member.DoesNotExist:
        return HttpResponse("���� ����� � ������ �� �������������.")

def logout(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass
    return HttpResponse("�� �����.")

def login(request):

    # ���� �� ��������� �����...
    if request.method == 'POST':

        # ���������, ��� ������� ��������� cookie:
        if request.session.test_cookie_worked():

            # ������� ���������, ������� �������� cookie.
            request.session.delete_test_cookie()

            # �� �������� ��� ����������� ����� ������ ��� ��������
            # ������ � ������, �� ��� ��� ��� ����� ���� ������...
            return HttpResponse("You're logged in.")

        # �������� �� ������, ���������� ��������� �� ������.
        # �� ��������� ����� ��� ����������� ���������� ��� ����������.
        else:
            return HttpResponse("Please enable cookies and try again.")

    # ���� �� �� �������� �����, ���������� �������� cookie
    # ������ � ������ ��������������.
    request.session.set_test_cookie()
    return render_to_response('foo/login_form.html')

	