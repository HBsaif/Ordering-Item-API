# Generated by Django 4.1.4 on 2023-01-05 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_my_API', '0005_remove_item_price_item_charity'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CharityRegistration',
        ),
        migrations.DeleteModel(
            name='UserRegistration',
        ),
        migrations.RemoveField(
            model_name='item',
            name='Charity',
        ),
    ]
