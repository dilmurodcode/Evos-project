# Generated by Django 5.2 on 2025-04-12 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_rename_lng_location_lon_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='region',
            field=models.CharField(choices=[('Tashkent', 'Tashkent shahri'), ('Tashkent region', 'Tashkent region'), ('Andijon', 'Andijon'), ('Fargʻona', 'Fargʻona'), ('Namangan', 'Namangan'), ('Samarqand', 'Samarqand'), ('Buxoro', 'Buxoro'), ('Navoiy', 'Navoiy'), ('Qashqadaryo', 'Qashqadaryo'), ('Surxondaryo', 'Surxondaryo'), ('Sirdaryo', 'Sirdaryo'), ('Jizzax', 'Jizzax'), ('Xorazm', 'Xorazm'), ('Qoraqalpogʻiston', 'Qoraqalpogʻiston Respublikasi')], default='Tashkent region'),
        ),
    ]
