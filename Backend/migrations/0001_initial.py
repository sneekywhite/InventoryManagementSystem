# Generated by Django 5.0.6 on 2024-07-01 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('supplier_email', models.EmailField(blank=True, max_length=255)),
                ('supplier_phone', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField(null=True)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('suppliers', models.ManyToManyField(related_name='items', to='Backend.supplier')),
            ],
        ),
    ]