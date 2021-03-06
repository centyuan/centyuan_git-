# Generated by Django 2.1.3 on 2018-11-19 21:06

import DjangoUeditor.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateTimeField(default=django.utils.timezone.now, verbose_name='日期')),
                ('count', models.IntegerField(default=0, verbose_name='访问量')),
            ],
            options={
                'verbose_name': '单日访问量',
                'verbose_name_plural': '单日访问量',
            },
        ),
        migrations.CreateModel(
            name='UseripNum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=30, verbose_name='ip地址')),
                ('numbers', models.IntegerField(verbose_name='访问次数')),
                ('time', models.DateTimeField(auto_now=True, verbose_name='最新访问时间')),
            ],
            options={
                'verbose_name': 'ip访问量',
                'verbose_name_plural': 'ip访问量',
            },
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='click_nums',
            field=models.IntegerField(default=0, verbose_name='点击量'),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='content',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='正文'),
        ),
    ]
