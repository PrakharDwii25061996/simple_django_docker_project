from django.shortcuts import render
from django.http import HttpResponse


def product_create(request):
	return render(request, 'product/product_create.html', {})
