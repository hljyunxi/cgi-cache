#!/usr/bin/python
#coding: utf8
#Author: chenyunyun<hljyunxi@gmail.com>


class CgiCacheError(Exception):
    pass

class NotImplementError(CgiCacheError):
    pass

class CacheKeyFormatError(CgiCacheError):
    pass
