# Generated by Django 3.2.6 on 2021-08-15 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_person_age'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='name',
            new_name='heading',
        ),
    ]
