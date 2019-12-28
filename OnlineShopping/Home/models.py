from django.db import models


class ProductDescription(models.Model):
    p_id = models.CharField(max_length=20, default='')
    item = models.CharField(max_length=20, default='')
    price = models.FloatField(max_length=9)
    rating = models.IntegerField()
    specs = models.CharField(max_length=500, default='')
    images = models.CharField(max_length=30, default='')
    company = models.CharField(max_length=20, default='Not Available')


class OrderDetails(models.Model):
    user_id = models.CharField(max_length=20)
    o_date = models.DateField('date published')
    price = models.FloatField(max_length=10)
    p_id = models.ForeignKey(ProductDescription, on_delete=models.CASCADE,)
    quantity = models.IntegerField(default=1)
    images = models.CharField(max_length=30, default='')
    item = models.CharField(max_length=20, default='')


class OrderHistory(models.Model):
    user_id = models.CharField(max_length=20)
    o_date = models.DateField('date published')
    price = models.FloatField(max_length=10)
    p_id = models.ForeignKey(ProductDescription, on_delete=models.CASCADE,)
    quantity = models.IntegerField(default=1)
    images = models.CharField(max_length=30, default='')
    item = models.CharField(max_length=20, default='')


class Ratings(models.Model):
    user_id = models.CharField(max_length=20, default='')
    p_id = models.CharField(max_length=20, default='')
    rating = models.IntegerField()
    feedback = models.CharField(max_length=200, default='')
