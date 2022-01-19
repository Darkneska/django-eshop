from django.urls import path

from . import views

urlpatterns = [
	path('', views.homepage, name='home'),
	path('shop/', views.shop, name='shop'),
	path('reservation/', views.reservation, name='reservation'),
	path('about/', views.about, name='about'),
	path('detail/', views.detail, name='detail'),
	path('bag/', views.bag, name='bag'),
	path('checkout/', views.checkout, name='checkout'),

]
