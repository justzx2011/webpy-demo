# -*- coding: utf-8 -*-
import web
import os, sys
import json
from web.template import render, Render
class demo():
    def __init__(self):
        print '==============================';
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
        if(input['act']):
            ret = {"errcode":0, "msg":"成功"};
        else:
            ret = {"errcode":1, "msg":"错误的方法" };
        return  demo(ret);
