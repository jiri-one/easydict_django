# Generated by Django 4.0.5 on 2022-07-27 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_alter_record_special_cze_alter_record_special_eng'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='special_cze',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Special notes'),
        ),
        migrations.AlterField(
            model_name='record',
            name='special_eng',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Special notes'),
        ),
    ]
