
from django.conf.urls import url, include
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^cities/', include('cities.urls')),
    url(r'^login/', include('login.urls')),
    url(r'^', include('mainpage.urls')),
    url(r'^products/', include('products.urls')),
    url(r'^orders/', include('orders.urls')),
    url(r'^', include('mainpage.urls')),
]
