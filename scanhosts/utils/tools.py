"""
File: tools.py
Author: lvah
Date: 2019-12-19 
Connect: 976131979@qq.com
Description: 

"""
import logging

from django.core.mail import send_mail
from datetime import datetime
from first_devops import settings


class SendMail(object):
    """发送邮件的封装类"""
    def __init__(self, subject, message, recipient_list, ):
        # 给每个邮件的标题加上当前时间， 时间格式为年月日_小时分钟秒_传入的邮件标题
        subject_time = datetime.now().strftime('%Y%m%d_%H%M%S_')
        self.recipient_list = recipient_list
        self.subject = subject_time + subject
        self.message = message
    def send(self):
        try:
            send_mail(
                subject=self.subject,
                message=self.message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=self.recipient_list,
                fail_silently=False
            )
            return True
        except Exception as e:
            logging.error(str(e))
            return False
