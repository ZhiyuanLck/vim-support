vim9script
py3 << END
import vim, sys
from pathlib import Path
cwd = vim.eval('expand("<sfile>:p:h")')
cwd = Path(cwd) / '..' / 'python'
cwd = cwd.resolve()
sys.path.insert(0, str(cwd))
from pywrapper import *
END

var home = resolve(expand('<sfile>:p'))

def Test()
  exec "python3 test()"
enddef

command! T exec "source " .. home | call Test()
