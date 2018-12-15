# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import NameForm, ContactForm
from django.core.mail import send_mail
from .models import AuthorForm

# Create your views here.

def index(request):
    #return HttpResponse("fdsfdsfds")
    return render(request, 'course/index2.html')

def index2(request):
    context = {
        'data': '11111test',
    }
    return render(request, 'course/index2.html', context)

def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        context = {
            'form': form,
        }
        if form.is_valid():
            return HttpResponseRedirect('/course/thanks/')
    else:
        form = NameForm()
        context = {
            'form': form,
        }
    #context = {
    #    'form': form,
    #}
    return render(request, 'course/name.html', context)

def get_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        context = {
            'form': form,
        }
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['admin@admin.admin']
            if cc_myself:
                recipients.append(sender)
            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/course/thanks/')
    else:
	data = {
            'subject': 'hello',
            'message': '111213213',
            'sender': 'lll@sss',
            'cc_myself': True,
        }
        form = ContactForm(data)
        context = {
            'form': form,
        }
    #context = {
    #    'form': form,
    #}
    return render(request, 'course/contact.html', context)

def get_author(request):
    if request.method == 'POST':
        form = AuthorForm(instance=request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            title = form.cleaned_data['title']
            brith_date = form.cleaned_data['brith_date']
        return HttpResponseRediret('/course/thanks/')
         
    else:
        form = AuthorForm()
    context = {
        'form': form,
    }
    return render(request, 'course/author.html', context)

def yourname(request):
    context = {
        'name': 'name',
    }
    return render(request, 'course/thanks.html', context)

def thanks(request):
    context = {
        'data': 'Thanks',
    }
    return render(request, 'course/thanks.html', context)
