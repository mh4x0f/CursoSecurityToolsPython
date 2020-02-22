
from plugins import *
plugin_classes = plugin.Template.__subclasses__()
for p in plugin_classes:
    print('plugin {0:20} {0:20}'.format(p("socket").name),p("socket").version)
