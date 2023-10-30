# Generated by Django 4.2.6 on 2023-10-27 15:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('phonestore', '0005_phone_tags_alter_order_status_alter_phone_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='phonestore.customer'),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='phonestore.phone'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('in progress', 'in progress'), ('delivred', 'delivred'), ('Out of order', 'Out of order')], max_length=100, null=True),
        ),
    ]