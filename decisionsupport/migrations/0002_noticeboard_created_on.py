# Generated by Django 3.1.5 on 2021-02-15 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decisionsupport', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticeboard',
            name='created_on',
            field=models.DateTimeField(auto_now=True, verbose_name='Created On'),
        ),
    ]
