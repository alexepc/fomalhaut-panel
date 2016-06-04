# -*- coding: utf-8 -*-
# created by restran on 2016/04/14
from __future__ import unicode_literals, absolute_import
import redis
from common.utils import text_type
from api_dashboard import settings


class RedisHelper(object):
    """
    redis 连接助手
    """
    _client = None

    def __init__(self):
        if RedisHelper._client is None:
            self._create_redis_client()

    @classmethod
    def get_client(cls):
        if RedisHelper._client is None:
            cls._create_redis_client()

        return RedisHelper._client

    @classmethod
    def ping_redis(cls):
        """
        测试redis能否连通
        :return:
        """
        cls.get_client().ping()

    @classmethod
    def _create_redis_client(cls):
        """
        创建连接
        :return:
        """
        RedisHelper._client = redis.StrictRedis(
            host=settings.REDIS_HOST, port=settings.REDIS_PORT,
            db=settings.REDIS_DB, password=settings.REDIS_PASSWORD)

def check_text_content_type(content_type):
    """
    检查content_type 是否是文本类型
    :param content_type:
    :return:
    """
    content_type = text_type(content_type).lower()
    text_content_type = [
        'text',
        'application/json',
        'application/x-javascript',
        'application/x-www-form-urlencoded'
    ]
    return any(map(content_type.startswith, text_content_type))