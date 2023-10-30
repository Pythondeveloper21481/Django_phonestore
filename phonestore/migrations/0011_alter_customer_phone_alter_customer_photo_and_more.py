# Generated by Django 4.2.6 on 2023-10-29 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phonestore', '0010_alter_customer_phone_alter_order_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='photo',
            field=models.ImageField(blank=True, default='img/wallpaper1.jpg', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='phone',
            name='status',
            field=models.CharField(choices=[('availabe', 'availabe'), ('Out of order', 'Out of order')], max_length=100, null=True),
        ),
    ]
