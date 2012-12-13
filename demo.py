# -*- coding: utf-8 -*-
import web
import os, sys 
import json
from web.template import render, Render

sys.path.append(os.path.join(os.getcwd()+'/include'))
from service.blogservice import BlogService
class demo():
    def __init__(self):
		pass;
    def GET(self):
        input = web.input(act='')
        print json.dumps(input);
        if(input['act'] == ''):
            return '请求空';
        act = input['act']
        return getattr(self, act)();
    def echo(self):
        input = web.input(content="")
        return input['content']
    def test(self):
        demo = web.template.frender('templates/demo.html')
        input = web.input(act='')
        content = ''
        if(input['act']):
            ret = {"errcode":0, "msg":content};
        else:
            ret = {"errcode":1, "msg":"错误的方法" };
        #return  demo(ret);
        return json.dumps(ret)
if __name__ == "__main__":
     b = BlogService()
     print sys.path;
