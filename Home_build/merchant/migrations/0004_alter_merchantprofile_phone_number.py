# Generated by Django 3.2.7 on 2024-03-07 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchant', '0003_alter_productlist_product_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchantprofile',
            name='Phone_Number',
            field=models.IntegerField(null=True),
        ),
    ]
