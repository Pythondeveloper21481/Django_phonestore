# Generated by Django 4.2.6 on 2023-10-29 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phonestore', '0008_alter_customer_phone_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('delivred', 'delivred'), ('in progress', 'in progress'), ('Out of order', 'Out of order')], max_length=100, null=True),
        ),
    ]