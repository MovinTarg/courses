# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        courses = Course.objects.all()
        if len(postData['name']) < 5:
            errors["short_name"] = "Course name cannot be less than 5 characters long!"
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    objects = CourseManager()

class DescriptionManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        descriptions = Description.objects.all()
        if len(postData['description']) < 15:
            errors["short_description"] = "Course description cannot be less than 15 characters long!"
        return errors

class Description(models.Model):
    course = models.OneToOneField(Course, on_delete=models.CASCADE, related_name="description")
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    objects = DescriptionManager()

class Comment(models.Model):
    course = models.ForeignKey(Course, related_name = "comments")
    comment = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)