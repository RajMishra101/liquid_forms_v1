# Generated by Django 4.0.2 on 2022-05-22 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_remove_form_see_response'),
    ]

    operations = [
        migrations.CreateModel(
            name='Design',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.form')),
            ],
        ),
    ]