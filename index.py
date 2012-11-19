# -*- coding: utf-8 -*-
import web
web.header("Content-Type","text/plain; charset=utf-8")
urls = (
        '/', 'index'
)

render = web.template.render('templates/')
class index:
    def GET(self):

        return render.layout('小例子')  ;

app = web.application(urls, globals())
application = app.wsgifunc()
