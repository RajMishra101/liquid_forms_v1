# Generated by Django 4.0.2 on 2022-05-22 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_rename_background_design_background_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form',
            name='borderradius',
        ),
        migrations.AlterField(
            model_name='form',
            name='borderColor',
            field=models.CharField(default='#272124', max_length=20),
        ),
        migrations.AlterField(
            model_name='form',
            name='headingColor',
            field=models.CharField(default='#272124', max_length=20),
        ),
    ]