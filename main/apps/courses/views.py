# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

# Create your views here.
def index(req):
    context = {
        'courses': Course.objects.all()
    }
    return render(req, 'courses/index.html', context)

def add(req):
    errors = Course.objects.basic_validator(req.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(req, error, extra_tags=tag)
        return redirect('/')
    errors = Description.objects.basic_validator(req.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(req, error, extra_tags=tag)
        return redirect('/')
    Course.objects.create(name=req.POST['name'])
    Description.objects.create(course=Course.objects.last(), description=req.POST['description'])
    return redirect('/')

def comment(req, course_id):
    context = {
        'course': Course.objects.get(id = course_id),
        'comments': Comment.objects.filter(course = Course.objects.filter(id=course_id))
    }
    return render(req, 'courses/comments.html', context)

def nComment(req, course_id):
    context = {
        'course': Course.objects.get(id = course_id)
    }
    Comment.objects.create(course=Course.objects.get(id = course_id), comment=req.POST['comment'])
    return redirect('/{}/comment'.format(course_id), context)

def remove(req, course_id):
    context = {
        'course': Course.objects.get(id = course_id)
    }
    return render(req, 'courses/delete.html', context)

def delete(req, course_id):
    Course.objects.get(id = course_id).delete()
    return redirect('/')