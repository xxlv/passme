# -*- coding: utf-8 -*-

import sys
import imp
import os
from os import listdir
from os.path import isfile,join


# adapter list
sys.path.append('./adapters')
from  weibo import *
from qyqq import *

class PassMe:

    def __init__(self,user,passwd):
        self.user=user
        self.passwd=passwd
        self.adapter_path='./adapters'
        self._init_adapters()

    def check(self,adapter_name):
        for adapter in self.adapters:
            if adapter[0]==adapter_name:
                adapter=adapter[1]
                adapter.check(self.user,self.passwd)

    def checkAll(self):
        result =list()
        for adapter in self.adapters:
            adapter=adapter[1]
            checked_status=adapter.check(self.user,self.passwd)
            result.append(checked_status)
        return result

    def listAllAdapters(self):
        for adapter in self.adapters:
            print(adapter[0]+"\n")


    def _init_adapters(self):
        # TODO dynamicy
        self.adapters=[]
        # self.adapters=[["weibo",Weibo()]]
        self.adapters.append(['qyqq',Qyqq()])


if __name__=='__main__':

    passme=PassMe("user",'passwd')
    passme.checkAll()
    # passme.check("weibo")
