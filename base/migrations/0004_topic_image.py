# Generated by Django 4.0.6 on 2023-01-17 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_product_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='image',
            field=models.ImageField(null=True, upload_to='topic/'),
        ),
    ]
