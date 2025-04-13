from django.db import models

class PartnerApplication(models.Model):

    TYPE_CHOICES = [
        ('legal_entity', 'LEGAL_ENTITY'),
        ('individual', 'INDIVIDUAL'),
    ]

    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    company_name = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    inn = models.CharField(max_length=255)


class Location(models.Model):


    class RegionChoice(models.TextChoices):
        TASHKENT = "Tashkent", "Tashkent shahri"
        TASHKENT_REGION = "Tashkent region", "Tashkent region"
        ANDIJON = "Andijon", "Andijon"
        FARGONA = "Fargʻona", "Fargʻona"
        NAMANGAN = "Namangan", "Namangan"
        SAMARQAND = "Samarqand", "Samarqand"
        BUXORO = "Buxoro", "Buxoro"
        NAVOIY = "Navoiy", "Navoiy"
        QASHQADARYO = "Qashqadaryo", "Qashqadaryo"
        SURXONDARYO = "Surxondaryo", "Surxondaryo"
        SIRDARYO = "Sirdaryo", "Sirdaryo"
        JIZZAX = "Jizzax", "Jizzax"
        XORAZM = "Xorazm", "Xorazm"
        QORAQALPOQSTON = "Qoraqalpogʻiston", "Qoraqalpogʻiston Respublikasi"


    lat = models.CharField(max_length=255)
    lon = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    region = models.CharField(max_length=255, choices=RegionChoice, default=RegionChoice.TASHKENT_REGION)


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
        null=True
    )


class PartnerApplicationObjectImage(models.Model):
    file = models.FileField(upload_to="obj_images/")
    application = models.ForeignKey(
        PartnerApplication, on_delete=models.CASCADE,
        related_name='partner_applications'
    )
