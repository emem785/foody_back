from django.db import models

# Create your models here.

class FoodItem(models.Model):
	name = models.CharField(max_length=30,null=False)
	desc = models.CharField(max_length=30,null=False)
	price = models.CharField(max_length=30,null=False)
	imageName = models.CharField(max_length=30,null=False)


class MenuCategory(models.Model):
	foodCategory = models.CharField(max_length=30,null=False)
	svgName = models.CharField(max_length=30,null=False)
	food_items = models.ForeignKey(FoodItem,on_delete=models.CASCADE)
