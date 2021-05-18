# Generated by Django 3.1.7 on 2021-05-01 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='Năm sinh'),
        ),
        migrations.AddField(
            model_name='device',
            name='comment',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Chú thích'),
        ),
        migrations.AddField(
            model_name='order',
            name='comment',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Chú thích'),
        ),
        migrations.AddField(
            model_name='staff',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='Năm sinh'),
        ),
        migrations.AddField(
            model_name='staff',
            name='gender',
            field=models.CharField(choices=[('M', 'Ông'), ('F', 'Bà')], default='M', max_length=1, verbose_name='Giới tính'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Địa chỉ'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Số điện thoại'),
        ),
        migrations.AlterField(
            model_name='device',
            name='model',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='year_of_manufacture',
            field=models.DateField(blank=True, null=True, verbose_name='Năm sản xuất'),
        ),
        migrations.AlterField(
            model_name='order',
            name='device',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='delivery.device'),
        ),
        migrations.AlterField(
            model_name='order',
            name='staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='delivery.staff'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Địa chỉ'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
