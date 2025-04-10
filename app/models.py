from django.db import models


class User(models.Model):
    number = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)


class New(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=255)
    description = models.TextField()


class Branch(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField()
    lat = models.CharField(max_length=255)
    lng = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    start_work = models.DateTimeField()
    end_work = models.DateTimeField()
    created_at = models.DateTimeField()


class Certificate(models.Model):
    description = models.TextField()
    image = models.ImageField()
    order = models.PositiveIntegerField()


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(255)
    image = models.ImageField(upload_to='product_img')
    price = models.DecimalField(max_digits=10, decimal_places=10)
    description = models.TextField()
    category = models.ForeignKey(
        Category, related_name="old_orders", on_delete=models.CASCADE,
    )


