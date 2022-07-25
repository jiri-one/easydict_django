# Generated by Django 4.0.5 on 2022-07-25 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cz', models.CharField(max_length=200, verbose_name='Word in CZech')),
                ('en', models.CharField(max_length=200, verbose_name='Word in ENglish')),
                ('notes', models.CharField(max_length=200, verbose_name='Notes about translation')),
                ('special', models.CharField(max_length=200, verbose_name='Special notes')),
                ('translator', models.CharField(max_length=200, verbose_name='Name of translator')),
            ],
        ),
    ]