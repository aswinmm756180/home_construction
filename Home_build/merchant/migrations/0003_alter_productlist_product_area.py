# Generated by Django 3.2.7 on 2024-03-06 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchant', '0002_productlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productlist',
            name='Product_area',
            field=models.CharField(choices=[('con', 'con'), ('electricals', 'electricals'), ('plumbing', 'plumbing'), ('interior', 'interior'), ('paint', 'paint'), ('courtyard', 'courtyard')], default='Calicut', max_length=200),
        ),
    ]
