# Generated by Django 4.0.2 on 2022-05-22 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_remove_form_borderradius_alter_form_bordercolor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form',
            name='background_image',
        ),
        migrations.RemoveField(
            model_name='form',
            name='header',
        ),
    ]
