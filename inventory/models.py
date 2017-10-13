from django.db import models

# Create your models here.
class Product(models.Model):
    productCode = models.CharField(max_length=50, unique=True, null=False)
    productName = models.CharField(max_length=200)
    productDesc = models.TextField()
    createDate = models.DateTimeField(auto_now_add=True)
    createUser = models.CharField(max_length=20)
    modifyDate = models.DateTimeField(auto_now_add=True)
    modifyUser = models.CharField(max_length=20)

    class Meta:
        ordering = ('productCode',)

