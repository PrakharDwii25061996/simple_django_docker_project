from django.db import models


class Item(models.Model):
	name = models.CharField(max_length=55)
	price = models.FloatField(max_length=100, default=0)
	description = models.TextField(null=True)
	number_of_items = models.IntegerField(default=1)
