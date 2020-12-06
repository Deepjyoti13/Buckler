from django.db import models

# Create your models here.
class product(models.Model):
    categoryChoice = (
        ('Women', 'Women'),
        ('Men', 'Men'),
        ('Kids', 'Kids'),
        ('Others', 'Others'),
        ('Special Deals', 'Special Deals'),
    )
    subCategoryChoice = (
        ('Casuals', 'Casuals'),
        ('Formals', 'Formals'),
        ('Sports', 'Sports'),
        ('Ethnic Wears', 'Ethnic Wears'),
        ('Winter Wears', 'Winter Wears'),
    )
    name = models.CharField(max_length=100)
    desc = models.TextField()
    date = models.DateField(auto_now_add=True)
    price = models.IntegerField()
    hashCode = models.CharField(max_length=60)
    category = models.CharField(max_length=60, choices=categoryChoice, null=True, blank=True)
    subcategory = models.CharField(max_length=60, choices=subCategoryChoice, null=True, blank=True)
    image = models.ImageField(upload_to='shop')
    shipped = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    trackingID = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name