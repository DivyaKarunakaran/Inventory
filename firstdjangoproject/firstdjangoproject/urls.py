
from django.conf.urls import url
from django.contrib import admin

from Inventory import views

urlpatterns = [
	url(r'^$',views.index,name='index'),
	url(r'^item/(?P<id>\d+)/', views.item_detail, name='item_detail'),
    url(r'^admin/', admin.site.urls),
	
]
