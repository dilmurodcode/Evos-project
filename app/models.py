from django.db import models

class PartnerApplication(models.Model):

    TYPE_CHOICES = [
        ('legal_entity', 'LEGAL_ENTITY'),
        ('individual', 'INDIVIDUAL'),
    ]

    app_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    company_name = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    inn = models.CharField(max_length=255)


class Location(models.Model):

    REGION_CHOICES = [
        ('tashkent', 'TASHKENT'),
        ('bukhara', 'BUXORO'),
        ('samarqand', 'SAMARQAND'),
        ('fargona', 'FARGONA'),
        ('navoiy', 'NAVOIY'),
        ('andijon', 'ANDIJON'),
        ('namangan', 'NAMANGAN'),
        ('jizzax', 'JIZZAX'),
        ('sirdaryo', 'SIRDARYO'),
        ('surxandaryo', 'SURXANDARYO'),
        ('qashqadaryo', 'QASHQADARYO'),
        ('xorazm', 'XORAZM'),
    ]

    lat = models.CharField(max_length=255)
    lon = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    region = models.CharField(max_length=20, choices=REGION_CHOICES)


class PartnerApplicationObject(models.Model):

    TYPE_CHOICES = [
        ('land', 'LAND'),
        ('commercial_building', 'COMMERCIAL_BUILDING'),
    ]

    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    floor = models.PositiveIntegerField(default=0)
    area = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    rent = models.PositiveIntegerField(default=0)
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE,
        related_name='partner_application_objects',
        null=True, blank=True
    )


class PartnerApplicationObjectImage(models.Model):
    file = models.FileField(upload_to="obj_images/")
    application = models.ForeignKey(
        PartnerApplicationObject, on_delete=models.CASCADE,
        related_name='partner_applications', null=True, blank=True
    )


class User(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)


class UserLocation(models.Model):
    lat = models.CharField(max_length=255)
    lon = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='userLoc', null=True, blank=True
    )


class UserCard(models.Model):
    user = models.CharField(max_length=255)
    card_ud = models.CharField(max_length=255)
    card_en = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=255)


class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    body = models.CharField(max_length=255)


class VacancyApplication(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    cv = models.FileField(upload_to="obj_cv/")
    vacancy = models.ForeignKey(
        Vacancy, on_delete=models.CASCADE,
        related_name='vacancyApplication', null=True, blank=True
    )


class Career(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='obj_images/')
    text = models.CharField(max_length=255)



class Category(models.Model):
    name = models.CharField(max_length=255)
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.id}-{self.name}"


class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='obj_images/')
    description = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    discount_price = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        related_name='product', null=True, blank=True
    )


class Order(models.Model):
    user = models.CharField(max_length=255)
    amount = models.CharField(max_length=255)
    status = models.CharField(max_length=255)


class OrderProduct(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name='orderProduct', null=True, blank=True
    )
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE,
        related_name='order', null=True, blank=True
    )
    amount = models.CharField(max_length=255)


class Branch(models.Model):
    name = models.CharField(max_length=255)
    order = models.IntegerField(default=0)
    image = models.ImageField(upload_to='obj_images/')
    duration = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    lon = models.CharField(max_length=255)
    lat = models.CharField(max_length=255)


class New(models.Model):
    title = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='obj_images/')
    body = models.CharField(max_length=255)


class AboutUs(models.Model):
    key = models.ImageField(upload_to='obj_image/')
    value = models.CharField(max_length=255)

    objects = models.Manager()


class History(models.Model):
    title = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='obj_images/')
    body = models.CharField(max_length=255)



class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)


class Feedback(models.Model):
    full_name = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    source = models.ImageField(upload_to='obj_images/')


class UserEmail(models.Model):
    email = models.EmailField(max_length=254)


class Certificate(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='obj_images/')
