import vim
import re

from typing import Union


class PopupOptDict(object):
    pass


class PopupPos:
    #  __valid_keys = ('line', 'col', 'pos', 'posinvert')
    def __init__(self,
            line      : Union[int, str, None] = None,
            col       : Union[int, str, None] = None,
            pos       : Union[str, None]      = None,
            posinvert : Union[bool, None]     = None,
            ):
        self.line      = line
        self.col       = col
        self.pos       = pos
        self.posinvert = posinvert

    def __str__(self):
        return str(dict(filter(lambda elem: elem[1] is not None, self.opt_dict.items())))

    @property
    def opt_dict(self) -> dict:
        return {
                "line":      self.line,
                "col":       self.col,
                "pos":       self.pos,
                "posinvert": self.posinvert,
                }

    def _check_set(self, value: Union[int, str, None], opt: str):
        if isinstance(value, str) and (
                value != "cursor" or
                re.match(r'cursor[+-]\d+$', value) is not None):
            raise ValueError(f"""value of popup option "{opt}" should not be "cursor", or something like "cursor+1" and "cursor-1" """)
        elif isinstance(value, (int, type(None))):
            if opt == "line":
                self.__line = value
            elif opt == "col":
                self.__col = value
        else:
            raise ValueError(f"""value of popup option "{opt}" of type `{type(value)}` should have type of `int` or `str`""")

    @property
    def line(self):
        return self.__line

    @line.setter
    def line(self, val: Union[int, str, None]):
        self._check_set(val, "line")

    @property
    def col(self):
        return self.__col

    @col.setter
    def col(self, val: Union[int, str, None]):
        self._check_set(val, "col")

    @property
    def pos(self):
        return self.__pos

    @pos.setter
    def pos(self, val: Union[str, None]):
        if not isinstance(val, str):
            raise ValueError(f"""value of popup option "pos" of type `{type(val)}` should have type of `str` or `None`""")
        elif val is None or val in ["topleft", "topright", "botleft", "botright", "center"]:
            self.__pos = val
        else:
            raise ValueError(f"""invalid value {val} of popup option `pos`""")

    @property
    def posinvert(self):
        return self.__posinvert

    @pos.setter
    def posinvert(self, val: Union[bool, None]):
        if not isinstance(val, (bool, type(None))):
            raise ValueError(f"""value of popup option "posinvert" of type `{type(val)}` should have type of `bool` or `None`""")
        else:
            self.__posinvert = val


class PopupOpt(object):
    """popup options"""
    def __init__(self,
            line      : Union[int, str, None] = None,
            col       : Union[int, str, None] = None,
            pos       : Union[str, None]      = None,
            posinvert : Union[bool, None]     = None,
            textprop=None,
            textpropwin=None,
            textpropid=None,
            fixed=None,
            flip=None,
            maxheight=None,
            minheight=None,
            maxwidth=None,
            minwidth=None,
            firstline=None,
            hidden=None,
            tabpage=None,
            title=None,
            wrap=None,
            drag=None,
            resize=None,
            close=None,
            highlight=None,
            padding=None,
            border=None,
            borderhighlight=None,
            borderchars=None,
            scrollbar=None,
            scrollbarhighlight=None,
            thumbhighlight=None,
            zindex=None,
            mask=None,
            time=None,
            moved=None,
            mousemoved=None,
            cursorline=None,
            filter=None,
            mapping=None,
            filtermode=None,
            callback=None,
            ):
        self.__line = line
        self.__col = col
        self.__pos = pos
        self.__posinvert = posinvert
        self.__textprop = textprop
        self.__textpropwin = textpropwin
        self.__textpropid = textpropid
        self.__fixed = fixed
        self.__flip = flip
        self.__maxheight = maxheight
        self.__minheight = minheight
        self.__maxwidth = maxwidth
        self.__minwidth = minwidth
        self.__firstline = firstline
        self.__hidden = hidden
        self.__tabpage = tabpage
        self.__title = title
        self.__wrap = wrap
        self.__drag = drag
        self.__resize = resize
        self.__close = close
        self.__highlight = highlight
        self.__padding = padding
        self.__border = border
        self.__borderhighlight = borderhighlight
        self.__borderchars = borderchars
        self.__scrollbar = scrollbar
        self.__scrollbarhighlight = scrollbarhighlight
        self.__thumbhighlight = thumbhighlight
        self.__zindex = zindex
        self.__mask = mask
        self.__time = time
        self.__moved = moved
        self.__mousemoved = mousemoved
        self.__cursorline = cursorline
        self.__filter = filter
        self.__mapping = mapping
        self.__filtermode = filtermode
        self.__callback = callback
        self.__opt_dict = {
                "line": line,
                "col": col,
                "pos": pos,
                "posinvert": posinvert,
                "textprop": textprop,
                "textpropwin": textpropwin,
                "textpropid": textpropid,
                "fixed": fixed,
                "flip": flip,
                "maxheight": maxheight,
                "minheight": minheight,
                "maxwidth": maxwidth,
                "minwidth": minwidth,
                "firstline": firstline,
                "hidden": hidden,
                "tabpage": tabpage,
                "title": title,
                "wrap": wrap,
                "drag": drag,
                "resize": resize,
                "close": close,
                "highlight": highlight,
                "padding": padding,
                "border": border,
                "borderhighlight": borderhighlight,
                "borderchars": borderchars,
                "scrollbar": scrollbar,
                "scrollbarhighlight": scrollbarhighlight,
                "thumbhighlight": thumbhighlight,
                "zindex": zindex,
                "mask": mask,
                "time": time,
                "moved": moved,
                "mousemoved": mousemoved,
                "cursorline": cursorline,
                "filter": filter,
                "mapping": mapping,
                "filtermode": filtermode,
                "callback": callback,
                }

    @property
    def line(self):
        return self.__line

    @line.setter
    def line(self, x):
        if isinstance(x, int) and x < 0:
            raise ValueError("""value of popup option "line" should not be negative""")
        elif isinstance(x, str) and (
                x != "cursor" or
                re.match(r'cursor[+-]\d+$', x) is not None):
            raise ValueError("""value of popup option "line" should not be "cursor", or something like "cursor+1" and "cursor-1" """)
        elif x is not None:
            raise ValueError("""value of popup option "line" should have type `int` or `str`""")
        else:
            self.__line = x

    def get_option(self, opt):
        return self.__opt_dict[opt]
