from django.db import models


class ProductType(models.Model):
    title = models.CharField(max_length=32)

    
    
class Category(models.Model):
    name = models.CharField(max_length=255)
    #برای مصتل کردن فیلد به عنوان کلید خارجی از سلف استفاده میکنید
    parent = models.ForeignKey('self', on_delete=models.CASCADE)
\
    

class Brand(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE)

  
    
class ProductAttribute(models.Model):
    INTEGER = 1
    STRING = 2
    FLOAT = 3
    
    ATTRIBUTE_TYPES_FILTERS = (
        (INTEGER, "integer"),
        (STRING, "string"),
        (FLOAT, "float")
    )
    
    title = models.CharField(max_length=255)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name="products")
    attribute_type = models.PositiveSmallIntegerField(default=INTEGER, choices=ATTRIBUTE_TYPES_FILTERS)
    
    
 
class Product(models.Model):
    upc = models.BigIntegerField(unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    product_type = models.ForeignKey(ProductType, on_delete=models.PROTECT)
    category_id = models.ForeignKey(Category , on_delete=models.PROTECT, related_name="products")
    brand_id = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name="products")



class ProductAttributeValue(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="attribute_value")
    value = models.CharField(max_length=40)
    attrinute = models.ForeignKey(ProductAttribute, on_delete=models.PROTECT, related_name="value")
    