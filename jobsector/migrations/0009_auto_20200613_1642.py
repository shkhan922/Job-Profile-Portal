# Generated by Django 3.0.6 on 2020-06-13 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsector', '0008_jobprofile_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobsector',
            name='Coaching_institution',
            field=models.TextField(default='Coaching Institute'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobsector',
            name='hiring',
            field=models.TextField(default='hiring'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobsector',
            name='job_description',
            field=models.TextField(default='job description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobsector',
            name='locations',
            field=models.TextField(default='location'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobsector',
            name='qualification',
            field=models.TextField(default='qualification'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobsector',
            name='responsibilties',
            field=models.TextField(default='responsibilities'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobsector',
            name='salary',
            field=models.TextField(default='salary'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobsector',
            name='skills',
            field=models.TextField(default='skills'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobsector',
            name='summary',
            field=models.TextField(default='summary'),
            preserve_default=False,
        ),
    ]
