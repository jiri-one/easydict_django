# Generated by Django 4.0.5 on 2022-07-26 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='cz',
            new_name='cze',
        ),
        migrations.RenameField(
            model_name='record',
            old_name='en',
            new_name='eng',
        ),
        migrations.RemoveField(
            model_name='record',
            name='notes',
        ),
        migrations.RemoveField(
            model_name='record',
            name='special',
        ),
        migrations.AddField(
            model_name='record',
            name='notes_cze',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Notes about translation'),
        ),
        migrations.AddField(
            model_name='record',
            name='notes_eng',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Notes about translation'),
        ),
        migrations.AddField(
            model_name='record',
            name='special_cze',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Special notes'),
        ),
        migrations.AddField(
            model_name='record',
            name='special_eng',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Special notes'),
        ),
        migrations.AddField(
            model_name='record',
            name='time_added',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date of addition'),
        ),
        migrations.AddField(
            model_name='record',
            name='time_changed',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date of change'),
        ),
        migrations.AlterField(
            model_name='record',
            name='translator',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Name of translator'),
        ),
    ]
