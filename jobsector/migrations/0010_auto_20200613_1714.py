# Generated by Django 3.0.6 on 2020-06-13 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobsector', '0009_auto_20200613_1642'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Jobsector',
            new_name='Jobprofiles',
        ),
        migrations.RenameModel(
            old_name='Jobcategory',
            new_name='Jobsectors',
        ),
        migrations.DeleteModel(
            name='Jobprofile',
        ),
    ]