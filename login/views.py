# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import UserForm
from django.shortcuts import render

def index(request):
	form = UserForm(request.POST or None)
	if request.method == "POST" and form.is_valid():
		data = form.cleaned_data
		print(data["name"])
		new_form = form.save()
		# return HttpResponseRedirect('/thanks/')
	return render(request, 'login/login.html', locals())