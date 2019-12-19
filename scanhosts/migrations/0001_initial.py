# Generated by Django 2.2.5 on 2019-12-19 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserIPInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(default='', max_length=150, verbose_name='IP地址')),
                ('time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '用户访问地址信息表',
                'verbose_name_plural': '用户访问地址信息表',
                'db_table': 'user_IP_info',
            },
        ),
    ]