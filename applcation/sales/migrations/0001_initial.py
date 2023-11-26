# Generated by Django 4.2.7 on 2023-11-26 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SalesData',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('purchaser_name', models.CharField(max_length=255)),
                ('item_description', models.CharField(max_length=255)),
                ('item_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('purchase_count', models.IntegerField()),
                ('merchant_address', models.CharField(max_length=255)),
                ('merchant_name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Venda',
                'verbose_name_plural': 'Vendas',
            },
        ),
    ]
