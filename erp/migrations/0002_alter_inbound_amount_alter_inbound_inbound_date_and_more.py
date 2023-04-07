# Generated by Django 4.2 on 2023-04-07 01:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('erp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inbound',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='금액'),
        ),
        migrations.AlterField(
            model_name='inbound',
            name='inbound_date',
            field=models.DateField(auto_now_add=True, verbose_name='입고 날짜'),
        ),
        migrations.AlterField(
            model_name='inbound',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.product', verbose_name='상품'),
        ),
        migrations.AlterField(
            model_name='inbound',
            name='quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='수량'),
        ),
        migrations.AlterField(
            model_name='product',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='담당자'),
        ),
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='상품 코드'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name='상품 설명'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50, verbose_name='상품 이름'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(verbose_name='상품 가격'),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('F', 'Free')], max_length=1, verbose_name='사이즈'),
        ),
        migrations.CreateModel(
            name='Outbound',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='수량')),
                ('outbound_date', models.DateField(auto_now_add=True, verbose_name='출고 날짜')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='금액')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.product', verbose_name='상품')),
            ],
            options={
                'verbose_name_plural': 'outbound',
                'ordering': ['-outbound_date'],
            },
        ),
    ]
