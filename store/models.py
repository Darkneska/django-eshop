from django.db import models


# Create your models here.
# Category of products
class Category(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="static/cat_img/")

    def __str__(self):
        return self.title

# Product Detail
class Product(models.Model):
        title = models.CharField(max_length=200)
        image = models.ImageField(upload_to="static/cat_img/")
        slug=models.CharField(max_length=400)
        detail=models.TextField()
        specs=models.TextField()
        price=models.PositiveIntegerField()
        category=models.ForeignKey(Category,on_delete=models.CASCADE)
        status=models.BooleanField(default=True)

        def __str__(self):
            return self.title


