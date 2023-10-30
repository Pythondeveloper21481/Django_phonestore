# Generated by Django 4.2.6 on 2023-10-29 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phonestore', '0009_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(default='img/wallpaper1.jpg', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Out of order', 'Out of order'), ('in progress', 'in progress'), ('delivred', 'delivred'), ('pending', 'pending')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='status',
            field=models.CharField(choices=[('Out of order', 'Out of order'), ('availabe', 'availabe')], max_length=100, null=True),
        ),
    ]