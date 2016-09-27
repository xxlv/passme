# -*- coding: utf-8 -*-

from adapter import Adapter


class Weibo(Adapter):

    def __init__(self):
        super(Weibo,self).__init__()
        self.auth_url='weibo.url'


    def check(self,user,passwd):
        self.logger.info("Check pass for weibo "+self.auth_url )
        checked_status=[0,'success']
        self.estimate(checked_status)
        return checked_status
