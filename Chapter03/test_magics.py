from IPython.core.magic import (register_line_magic, register_cell_magic)
import subprocess
import re

@register_line_magic
def fortune(line):
    p1 = subprocess.Popen(["/usr/bin/fortune",  "-l"], stdout=subprocess.PIPE)
    ret = str(p1.communicate()[0], 'utf-8')
    print(ret)
    return 0

@register_cell_magic
def story(line, cell):
    p1 = subprocess.Popen(["/usr/bin/fortune",  "-l"], stdout=subprocess.PIPE)
    str = (p1.communicate( )[0]).decode('utf-8')
    target = cell.replace("\n", "")

    while (re.search(target, str) == None):
        p1 = subprocess.Popen(["/usr/bin/fortune",  "-l"], stdout=subprocess.PIPE)
        str = (p1.communicate( )[0]).decode('utf-8')

    print(str)
    return 0

del fortune
