# Generated by Django 2.1.5 on 2019-06-26 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20190626_0948'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='product',
            unique_together={('title', 'slug')},
        ),
    ]
