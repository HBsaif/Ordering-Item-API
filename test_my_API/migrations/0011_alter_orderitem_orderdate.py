# Generated by Django 4.1.4 on 2023-01-10 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_my_API', '0010_orderitem_orderdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='OrderDate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]