# Generated by Django 4.0 on 2023-11-08 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0005_rename_church_program_churchprogram'),
    ]

    operations = [
        migrations.CreateModel(
            name='MembersList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=200)),
                ('last_name', models.CharField(default='', max_length=200)),
                ('email', models.CharField(default='', max_length=200)),
                ('phone', models.CharField(default='', max_length=200)),
                ('country', models.CharField(default='', max_length=200)),
                ('address', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
