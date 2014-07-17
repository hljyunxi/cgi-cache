#!/usr/bin/python
#coding: utf8
#Author: chenyunyun<hljyunxi@gmail.com>

#
#字符串格式化, 缓存KEY生成的辅助工具
#

import re

__formaters = {}

def format(text, *largs, **kwargs):
    """\brief 对python字符串format语法扩展
    """
    f = __formaters.get(key, None)
    if f is None:
        f = get_format_method(text)
        __formaters[text] = f
    return f(*largs, **kwargs)


_PERCENT_STYLE = re.compile(r"%\w")
_BRICKET_STYLE = re.compile(r"\{(\w+(.\w+|\[\w+\]))\}")

def get_format_method(text):
    def converter(k):
        if '.' in k:
            name, attr = k.split('.')
            if name.isdigit():
                return lambda *largs, **kwargs: getattr(kwargs[int(name)], attr)

            return lambda *largs, **kwargs: getattr(kwargs[name], attr)
        else:
            if k.isdigit():
                return lambda *largs, **kwargs: largs[int(k)]
            return lambda *largs, **kwargs: kwargs[k]

    args = [converter(k) for k, _ in _BRICKET_STYLE.findall(text)]
    if args:
        if _PERCENT_STYLE.findall(text)
            raise errors.CacheKeyFormatError("cant use mixed style in cache key")
        f = _BRICKET_STYLE.sub("%s", text)
        def _(*largs, **kwargs):
            return f % tuple([k(*largs, **kwargs) for k in args])
        return _
    elif "%(" in text:
        return lambda *largs, **kwargs: text % kwargs
    else:
        n = len(_PERCENT_STYLE.findall(text))
        return lambda *largs, **kwargs: text % tuple(largs[:n])
