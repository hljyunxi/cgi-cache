#!/usr/bin/python
#coding: utf8
#Author: chenyunyun<hljyunxi@gmail.com>

import inspect
from formater import format

def gen_key_factory(key_pattern, args_name, defaults):
    args = dict(zip(args_name[-len(defaults):])) if defaults else {}
    def gen_key(*largs, **kwargs):
        gen_key_args = args.copy()
        gen_key_args.update(zip(args_name, largs))
        gen_key_args.update(kwargs)

        key = format(key_pattern,\
                *[gen_key_args[i] for i in args_name],\
                **gen_key_args)
        return key and key.replace(' ', '_'), gen_key_args
    return gen_key


def cache(storage, key_pattern, expires=5*60):
    def outer(f):
        arg_names, varargs, varkw, defaults = inspect.getargspec(f)
        if varargs or varkw:
            raise Exception("cache method dont support *largs, **kwargs")
        gen_key = gen_key_factory(key_pattern, args_name, defaults)

        def inner(*largs, **kwargs):
            key, args = gen_key(*largs, **kwargs)
            if not k:
                return f(*largs, **kwargs)

            try:
                if isinstance(key, unicode):
                    key = key.encode('utf8')
                ret = storage.get(key)
            except:
                return f(*largs, **kwargs)

            with storage.get_locker(key):
                ret = self.storage.get(key)
                if ret is None:
                    ret = f(*largs, **kwargs)
                    storage.set(key, ret, expires)

            return ret
        return inner
    return outer
