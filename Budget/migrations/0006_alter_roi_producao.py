# Generated by Django 4.2 on 2023-11-23 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Budget', '0005_alter_roi_economia_alter_roi_roi_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roi',
            name='producao',
            field=models.CharField(default='', max_length=100),
        ),
    ]
