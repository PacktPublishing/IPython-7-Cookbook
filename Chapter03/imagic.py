import re
import subprocess
import IPython.core.magic as ipym


@ipym.magics_class
class IMagic(ipym.Magics):
    
    def __init__(self, shell):
        super(IMagic, self).__init__(shell)

    @ipym.line_magic
    def ifortune(self, line):
        p1 = subprocess.Popen(["/usr/bin/fortune",  "-l"], stdout=subprocess.PIPE)
        ret = str(p1.communicate()[0], 'utf-8')
        print(ret)
        return 0
        
    @ipym.cell_magic
    def istory(self, line, cell):
        p1 = subprocess.Popen(["/usr/bin/fortune",  "-l"], stdout=subprocess.PIPE)
        str = (p1.communicate( )[0]).decode('utf-8')
        target = cell.replace("\n", "")

        while (re.search(target, str) == None):
            p1 = subprocess.Popen(["/usr/bin/fortune",  "-l"], stdout=subprocess.PIPE)
            str = (p1.communicate( )[0]).decode('utf-8')

        print(str)
        return 0


def load_ipython_extension(ip):
    i_magic = IMagic(ip)
    ip.register_magics(i_magic)

