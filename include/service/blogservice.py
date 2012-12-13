# -*- coding: utf-8 -*-
import redis
class BlogService:
    def __init__(self):
        print 'BlogService.__init__'
    def save(self,blog):
        print 'BlogService.save'
                
