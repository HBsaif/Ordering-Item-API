# Generated by Django 4.1.4 on 2023-01-10 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_my_API', '0008_item_charity'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=200)),
                ('Quantity', models.IntegerField()),
                ('Username', models.EmailField(max_length=254)),
                ('ItemId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_my_API.item')),
            ],
        ),
    ]