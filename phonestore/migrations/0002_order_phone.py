# Generated by Django 4.2.6 on 2023-10-21 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phonestore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('Out of order', 'Out of order'), ('delivred', 'delivred'), ('in progress', 'in progress'), ('pending', 'pending')], max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marque', models.CharField(max_length=100, null=True)),
                ('model', models.CharField(max_length=100, null=True)),
                ('price', models.FloatField(null=True)),
                ('category', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(max_length=100, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('photo', models.ImageField(null=True, upload_to='')),
                ('status', models.CharField(choices=[('Out of order', 'Out of order'), ('availabe', 'availabe')], max_length=100, null=True)),
            ],
        ),
    ]