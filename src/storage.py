#!/usr/bin/python
#coding: utf8
#Author: chenyunyun<hljyunxi@gmail.com>

import errors
import redis_helper

class Storage(object):
    def __init__(self):
        pass

    def set(self, key, value):
        raise errors.NotImplementError()

    def get(self, key):
        raise errors.NotImplementError()


class RedisStorage(Storage):
    def __init__(self, rdb):
        self.rdb = rdb
        super(Storage, self).__init__()

    def get(self, key):
        return self.rdb.get(key)

    def set(self, key, value):
        return self.rdb.set(key, value)
