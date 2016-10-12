# -*- coding: utf-8 -*-

from .adapter import Adapter


class Weibo(Adapter):

    def __init__(self):
        super(Weibo,self).__init__()
        self.auth_url=None
        self.name='Weibo'


    def check(self,user,passwd):
        if self.auth_url is None:
            return self.skip(" Not finished yet")


        self.logger.info("Check password for  "+self.auth_url )
        checked_status=[0,'success']
        self.estimate(checked_status)
        return checked_status
