# Generated by Django 4.0 on 2023-11-07 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0003_testimonial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='image',
            field=models.ImageField(default='', upload_to='testimony'),
        ),
    ]