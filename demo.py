# -*- coding: utf-8 -*-
import web
import os,sys
class demo():
    def __init__(self):
        print '==============================';
    def GET(self):
        input = web.input(act='')
        if(input['act'] == ''):
            return '请求空';
        act = input['act']
        print act;
        return getattr(self, act)();
    def echo(self):
        input = web.input(content="")
        return input['content']
    def test(self):
        return 'ok'