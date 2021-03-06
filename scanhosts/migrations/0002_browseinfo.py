# Generated by Django 2.2.5 on 2019-12-19 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scanhosts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrowseInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_agent', models.CharField(default='', max_length=100, null=True, verbose_name='用户浏览器信息')),
                ('disk_id', models.CharField(default='', max_length=256, verbose_name='唯一设备ID')),
                ('user_ip', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='scanhosts.UserIPInfo')),
            ],
            options={
                'verbose_name': '用户浏览器信息表',
                'verbose_name_plural': '用户浏览器信息表',
                'db_table': 'browse_info',
            },
        ),
    ]
