import vim
from functools import partial
from copy import copy


vimcmd = vim.command


def vimeval(cmd, wrapper=None):
    r = vim.eval(cmd)
    if wrapper is None:
        return r
    return wrapper(r)


def _vimget(namespace, prefix, var, default, wrapper=None):
    return vimeval(f"get({namespace}, '{prefix}_{var}', {default})", wrapper)


def special_get(*args, **kwargs):
    return partial(_vimget, *args, **kwargs)


def winexec(winid, cmd):
    vimcmd(f'call win_execute({winid}, "{cmd}")')


def setlocal(winid, option):
    vimcmd(f"call win_execute({winid}, 'setlocal {option}')")


def dplen(text):
    text = copy(text).replace("\\", "\\\\")
    return vimeval(f'strdisplaywidth("{text}")', int)


def bytelen(text):
    text = copy(text).replace("\\", "\\\\")
    return vimeval(f'len("{text}")', int)
