# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
	login = models.CharField(max_length=45)
	pwd = models.CharField(max_length=45)
	email = models.EmailField(blank=True, null=True, default=None)
	name = models.CharField(max_length=64, blank=True, null=True, default=None)

	def __str__(self):
		return "%s %s " % (self.login, self.email)