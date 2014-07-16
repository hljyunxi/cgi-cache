#!/usr/bin/python
#coding: utf8
#Author: chenyunyun<hljyunxi@gmail.com>

from redis import Redis, ConnectionPool

redis_conn_pool = ConnectionPool(
        host = '',\
        port =
        )

rdb = redis.Redis(connection_pool=redis_conn_pool)
