# Generated by Django 3.0.6 on 2020-06-11 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsector', '0005_auto_20200609_1946'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_main', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('overview', models.TextField()),
                ('thumbnail', models.ImageField(upload_to='')),
                ('featured', models.BooleanField()),
            ],
        ),
    ]