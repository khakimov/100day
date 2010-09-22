#coding: utf-8
from django.shortcuts import render_to_response, get_object_or_404
from cto.goal.models import Report, Goal
from django.contrib.auth.models import User, Permission
from django.contrib import auth
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
import re

# Create your views here.
def index(request):
    goals = Goal.objects.all()
    users = User.objects.all()
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        
        if not re.search(r'^\w+$', username): 
            print 'zashli v if'
            errors = 'В логине используйте буквы и цифры.'
            return render_to_response('index.html', { 'goals': goals, 'users': users, 'errors': errors, 'username': username, 'password': password })
        try: 
            User.objects.get(username=username) 
        except User.DoesNotExist: 
            user = User.objects.create_user(username, '', password)
            user.is_staff = True
            user.user_permissions.add('25', '26', '27', '28', '29', '30')
            user.save()
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return HttpResponseRedirect('/%s/' % username)       
            
            
        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            auth.login(request, user)
            # Redirect to a success page.
            #return render_to_response('index.html', { 'goals': goals, 'users': users, 'username': request.user.username })
            return HttpResponseRedirect('/%s/' % username)       
        else:
             # Show an error page
             errors = 'Ошибка. Причины может быть две: неверный пароль или логин уже занят.'
             return render_to_response('index.html', { 'goals': goals, 'users': users, 'errors': errors, 'username': username, 'password': password })
    else:       
        if request.user.is_authenticated(): 
            return render_to_response('index.html', { 'goals': goals, 'users': users, 'username': request.user.username })
        else:
            return render_to_response('index.html', { 'goals': goals, 'users': users })
            

def personal_day(request, user):
    profile = get_object_or_404(User, username=user)
    latest_messages = Report.objects.filter(user=profile).order_by('-publication_date')[:5]
    goals = Goal.objects.filter(user=profile)
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if not re.search(r'^\w+$', username): 
            print 'zashli v if'
            errors = 'В логине используйте буквы и цифры.'
            return render_to_response('countdown.html', { 'goals': goals,  'messages': latest_messages, 'errors': errors, 'username': username, 'password': password })
        try: 
            User.objects.get(username=username) 
        except User.DoesNotExist: 
            user = User.objects.create_user(username, '', password)
            user.is_staff = True
            user.user_permissions.add('40', '41', '42', '43', '44', '45')
            user.save()
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return render_to_response('countdown.html', { 'goals': goals,  'messages': latest_messages, 'username': request.user.username })
            
        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            auth.login(request, user)
            # Redirect to a success page.
            return render_to_response('countdown.html', { 'goals': goals, 'messages': latest_messages, 'username': request.user.username })
        else:
             # Show an error page
             errors = 'Ошибка. Причины может быть две: неверный пароль или логин уже занят.'
             return render_to_response('countdown.html', { 'goals': goals, 'messages': latest_messages, 'errors': errors, 'username': username, 'password': password })
    else:       
        if request.user.is_authenticated(): 
            return render_to_response('countdown.html', { 'goals': goals, 'messages': latest_messages, 'username': request.user.username })
        else:
            return render_to_response('countdown.html', { 'goals': goals, 'messages': latest_messages })

    

