# Generated by Django 3.1.7 on 2021-03-23 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('IT_help', '0002_auto_20210321_1540'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(default='', max_length=50)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('pic_url', models.CharField(max_length=255)),
                ('mtext', models.CharField(blank=True, max_length=255)),
                ('mdt', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
