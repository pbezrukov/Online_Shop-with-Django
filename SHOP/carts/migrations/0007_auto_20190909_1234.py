# Generated by Django 2.1.5 on 2019-09-09 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0006_cartitem_variations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='variations',
            field=models.ManyToManyField(to='products.Variation'),
        ),
    ]