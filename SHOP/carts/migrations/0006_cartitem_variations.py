# Generated by Django 2.1.5 on 2019-09-09 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_variation_category'),
        ('carts', '0005_auto_20190902_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='variations',
            field=models.ManyToManyField(blank=True, null=True, to='products.Variation'),
        ),
    ]
