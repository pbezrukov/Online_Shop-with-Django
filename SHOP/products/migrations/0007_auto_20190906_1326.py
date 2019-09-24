# Generated by Django 2.1.5 on 2019-09-06 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_variation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.ProductImage'),
        ),
    ]