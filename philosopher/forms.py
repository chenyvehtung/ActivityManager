#! /usr/bin/python
# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from philosopher.models import UserProfile, Activity, Application

class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ("username", "email",)
		lables = {
			'username': u'姓名',
			'email': u'邮箱',
		}

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		exclude = ("user", "attimes", "status", "intro", )
		lables = {
			'role': u'角色',
			'gender': u'性别',
			'schoolID': u'学工号',
			'phone': u'手机号码',
			'avatar': u'头像', 
		}

class EUserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ("username", "email", )
		lables = {
			'username': u'姓名',
			'email': u'邮箱',
		}

class EUserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		exclude = ("user", "attimes", "status", "role", )
		lables = {
			'intro': u'自我介绍',
			'gender': u'性别',
			'schoolID': u'学工号',
			'phone': u'手机号码',
			'avatar': u'头像', 
		}

class AddActivityForm(forms.ModelForm):
	class Meta:
		model = Activity
		exclude = ('atorganizer', 'atstatus', 'createdate', 'publishdate')

class ApplicationApplyForm(forms.ModelForm):
	class Meta:
		model = Application
		fields = ('phone', 'grade', 'applyreason', )
		lables = {
			'phone': u'手机号码',
			'grade': u'年级',
			'applyreason' : u'申请原因',
		}