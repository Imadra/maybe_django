# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *

class UserAdmin (admin.ModelAdmin):
	#list_display = ["name", "email"]
	list_display = [field.name for field in User._meta.fields]
	# exclude = ["email"]
	# field = ["email"]
	list_filter = ['name', ]
	search_filter = ['name', 'email']
	class Meta:
		model = User

admin.site.register(User, UserAdmin)