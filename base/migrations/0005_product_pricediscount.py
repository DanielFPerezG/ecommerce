# Generated by Django 4.0.6 on 2023-01-19 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_topic_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='priceDiscount',
            field=models.PositiveIntegerField(null=True),
        ),
    ]