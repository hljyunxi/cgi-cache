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


def cache(storage, key_pattern, expire=5*60, max_try=0):
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

            retry = max_retry
            while ret is None and retry > 0:
                # when node is down, add() will failed
                if storage.add(key + '#mutex', 1, int(max_retry * 0.1)):
                    break
                time.sleep(0.1)
                ret = storage.get(key)
                retry -= 1

            if ret is None:
                ret = f(*largs, **kwargs)
                if ret is not None:
                    storage.set(key, r, expire)
                if max_retry > 0:
                    storage.delete(key + '#mutex')
            return ret
        return inner
    return outer
