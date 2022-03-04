from django.db import models

# Create your models here.


class Store_add(models.Model):
    Name_of_Product = models.CharField(max_length=100)
    Price = models.BigIntegerField()
    Discount = models.DecimalField(max_digits=10, decimal_places=3)


    def get_sale(self):
        Discount_price = float(self.Discount) * float(self.Price / 100)
        return Discount_price
    def get_total(self):
        Total = float(self.Price) - (float(self.Discount) * float(self.Price / 100))
        return Total
