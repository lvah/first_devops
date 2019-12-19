from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from scanhosts.models import UserIPInfo, BrowseInfo
import json
import logging
logger = logging.getLogger('django')

# Create your views here.


def user_info(request):
    # request.META 是一个Python字典，包含了所有本次HTTP请求的Header信息，比如用户IP地址和用户Agent（通常是浏览器的名称和版本号）
    ip = request.META.get('REMOTE_ADDR')
    user_agent = request.META.get('HTTP_USER_AGENT')

    # 使用filter()方法对数据进行过滤, 返回的是列表， 列表元素是符合条件的对象。
    user_obj = UserIPInfo.objects.filter(ip=ip)

    # 如果没有找到，则新建UserIPInfo对象,并获取对象编号(为了和BrowseInfo表关联)
    if not user_obj:
        res = UserIPInfo.objects.create(ip=ip)
        user_ip_id = res.id
    else:
        logger.info('%s already exists' %(ip))
        user_ip_id = user_obj[0].id
    # 新建BrowseInfo对象
    BrowseInfo.objects.create(user_agent=user_agent, user_ip_id=user_ip_id)
    # 字典封装返回的数据信息
    result = {
        'STATUS': 'success',
        'INFO': 'User Info',
        'IP': ip,
        'User-Agent': user_agent
    }

    # 以json的方式封装返回， 下面的两种方式任选一种.
    # return  HttpResponse(json.dumps(result), content_type='application/json')
    return JsonResponse(result)


def user_history(request):
    # 获取UserIPInfo表的所有对象信息；
    ip_lists = UserIPInfo.objects.all()
    infos = {}
    # 获取每个IP访问网站浏览器的信息， 格式如下:
    """
    infos = {
        '127.0.0.1' : ['UA-1', 'ua-2'], 
        '172.25.254.1' : ['UA-1', 'ua-2'], 
    }
    """
    for item in ip_lists:
        infos[item.ip] = [b_obj.user_agent for b_obj in BrowseInfo.objects.filter(user_ip_id=item.id)]

    result = {
        'STATUS': 'success',
        'INFO': infos
    }

    return JsonResponse(result)
