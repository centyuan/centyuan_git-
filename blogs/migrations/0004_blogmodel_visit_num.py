# Generated by Django 2.1.3 on 2018-11-19 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20181119_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='visit_num',
            field=models.IntegerField(default=0, verbose_name='访问量'),
        ),
    ]
