from django.urls import path
from . import views


urlpatterns = [
	path('product/create/', views.product_create, name='product_create')
]
