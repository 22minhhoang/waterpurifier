# Generated by Django 3.1.7 on 2021-05-24 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0010_auto_20210525_0302'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device',
            old_name='model',
            new_name='model_code',
        ),
    ]
