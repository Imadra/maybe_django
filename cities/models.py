# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Cities(models.Model):
	name = models.CharField(max_length=45)
	name_rus = models.CharField(max_length=45)

	def __str__(self):
		return self.name
