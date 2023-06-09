# Generated by Django 4.2 on 2023-04-07 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0003_alter_outbound_options_alter_outbound_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inbound',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='비용'),
        ),
        migrations.AlterField(
            model_name='outbound',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='비용'),
        ),
    ]
