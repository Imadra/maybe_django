from __future__ import unicode_literals
from django.db import models
# -*- coding: utf-8 -*-

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=64, blank=True, null=True, default=None)
	description = models.TextField(blank=True, null=True, default=None)
	price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return "%s %s" % (self.price, self.name)

class ProductImage(models.Model):
	product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='./mainpage/static/img/products_img/')
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return "%s " % (self.id)