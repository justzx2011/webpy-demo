# -*- coding: utf-8 -*-
import web, os
from mako.filters import trim
import sys, os  


def notfound():
     return web.notfound('对不起Sorry, the page you were looking for was not found.')

def head_loadhook():
    web.header('Content-type', "text/html; charset=utf-8")
    
def import_modules(modules):
    urls = []
    g = globals()
    from imp import load_source
    def import_module(name, file):
        print name;
        m = load_source(name, file)
        g[name] = m
        urls.extend(['/%s' % name, '%s.%s' % (name, name)]);
        
    for (name, file) in modules:
        if name != 'index' and name not in g  :
            import_module(name, file)
            
    return urls

app_dir = os.getcwd();
modules = [(x[:-3], os.path.join(app_dir, x)) for x in os.listdir(app_dir) if x.endswith('.py')]
urls = import_modules(modules);
app = web.application(urls, globals(), autoreload=True)
app.notfound = notfound
app.add_processor(web.loadhook(head_loadhook))
web.config.debug = True
print '------------app run ---------------------'
print urls;
print modules;
application = app.wsgifunc()



