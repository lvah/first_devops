from django.db import models

# Create your models here.

"""
- 一个类对应一个数据库表；
- 类的一个属性对应数据库表的一个表头；
    - max_length: 字符串最大长度， 对应数据库的varchar类型
    - default: 指定默认值
    - verbose_name: 指定Django后台显示的列头信息
    - auto_now： 每次修改记录时自动更新为当前时间

- Meta类的设置
	- verbose_name： 指定Django后台显示的表名称单数
	- verbose_name_plural： 指定Django后台显示的表名称复数
	- db_table: 指定数据库表的名称， 默认是APP名称_类名称.
"""


class UserIPInfo(models.Model):
    ip = models.CharField(max_length=150, default='', verbose_name='IP地址')
    time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    class Meta:
        verbose_name = '用户访问地址信息表'
        verbose_name_plural = verbose_name
        db_table = 'user_IP_info'


class BrowseInfo(models.Model):
    # null=True: 是针对数据库而言，True表示数据库的该字段可以为空。
    user_agent = models.CharField(max_length=100, default='',
                                  verbose_name='用户浏览器信息', null=True)
    disk_id = models.CharField(max_length=256, default='', verbose_name='唯一设备ID')
    """
    ForeignKey是一种关联字段，将两张表进行关联的方式
    on_delete: 是否级联删除.Django1.x默认级联删除， Django2.x必须手动指定
    on_delete有CASCADE、PROTECT、SET_NULL、SET_DEFAULT、SET()五个可选择的值
        CASCADE：此值设置，是级联删除。
        PROTECT：此值设置，是会报完整性错误。
        SET_NULL：此值设置，会把外键设置为null，前提是允许为null。
        SET_DEFAULT：此值设置，会把设置为外键的默认值。
        SET()：此值设置，会调用外面的值，可以是一个函数。
    """
    user_ip = models.ForeignKey('UserIPInfo', on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = '用户浏览器信息表'
        verbose_name_plural = verbose_name
        db_table = 'browse_info'
