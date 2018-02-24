# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Users(models.Model):
	login = models.CharField(max_length=45)
	pwd = models.CharField(max_length=45)

	def __str__(self):
		return self.login