# Generated by Django 3.0.8 on 2020-07-08 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='surname',
            new_name='exame',
        ),
    ]
