
from django.conf.urls import url, include
from django.views.generic import ListView
from cities.models import Cities
from . import views

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Cities.objects.all().order_by("id"),
    	template_name="cities/cities.html")),
]
