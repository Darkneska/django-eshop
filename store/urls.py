from django.urls import path

from . import views

urlpatterns = [
	path('', views.homepage, name='home'),
	path('shop/', views.shop, name='shop'),
	path('reservation/', views.reservation, name='reservation'),
	path('about/', views.about, name='about'),
	path('checkout/', views.detail, name='checkout'),
	path('bag/', views.bag, name='bag'),
	path('product/<str:slug>', views.detail, name='detail'),

]
