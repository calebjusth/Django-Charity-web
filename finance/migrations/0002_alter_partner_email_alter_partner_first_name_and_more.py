# Generated by Django 4.0 on 2023-11-07 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='email',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='partner',
            name='first_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='partner',
            name='last_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='partner',
            name='phone',
            field=models.CharField(max_length=200),
        ),
    ]
