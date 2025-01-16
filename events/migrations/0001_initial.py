# Generated by Django 5.1.4 on 2025-01-08 11:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=255)),
                ('event_date', models.DateField()),
                ('sales_start_at', models.DateTimeField()),
                ('sales_end_at', models.DateTimeField()),
                ('ticket_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_tickets', models.IntegerField()),
                ('total_sold', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('paid_amount', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('payment_method', models.CharField(choices=[('SSLCOMMERZ', 'SSLCommerz')], max_length=10)),
                ('status', models.CharField(choices=[('INIT', 'Init'), ('PENDING', 'Pending'), ('CONFIRMED', 'Confirmed'), ('CANCELLED', 'Cancelled'), ('FAILED', 'Failed')], default='INIT', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SSLCommerzDatum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('val_id', models.CharField(max_length=100, null=True)),
                ('currency', models.CharField(max_length=10, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('store_amount', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('card_type', models.CharField(max_length=100, null=True)),
                ('card_no', models.CharField(max_length=100, null=True)),
                ('bank_tran_id', models.CharField(max_length=100, null=True)),
                ('tran_id', models.CharField(max_length=100, null=True)),
                ('status', models.CharField(max_length=100, null=True)),
                ('tran_date', models.DateTimeField(null=True)),
                ('currency_type', models.CharField(max_length=100, null=True)),
                ('currency_amount', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('currency_rate', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('base_fair', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('error', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sslcommerz_datum', to='events.order')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('CONFIRMED', 'Confirmed'), ('CANCELLED', 'Cancelled')], default='PENDING', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='events.event')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='ticket',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='events.ticket'),
        ),
    ]
