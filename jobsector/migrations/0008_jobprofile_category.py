# Generated by Django 3.0.6 on 2020-06-13 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsector', '0007_auto_20200612_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobprofile',
            name='category',
            field=models.ManyToManyField(to='jobsector.Jobcategory'),
        ),
    ]
