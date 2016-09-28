# -*- coding: utf-8 -*-

import sys
import imp
import os
import argparse

from os import listdir
from os.path import isfile,join


import coloredlogs
# adapter list
sys.path.append('./adapters')

from weibo import Weibo
from qyqq import Qyqq
from github import Github
from redmine import Redmine


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
        self.adapters.append(['qyqq',Qyqq()])
        self.adapters.append(['github',Github()])
        self.adapters.append(['redmine',Redmine()])



if __name__=='__main__':

    coloredlogs.install()

    parser = argparse.ArgumentParser(description='Passme! check your password')
    parser.add_argument('-u', action="store", help="user identity")
    parser.add_argument('-p', action="store", help="user password")
    parser.add_argument('-a', action="store", help="adapter specify")
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')

    results = parser.parse_args()
    user=results.u
    passwd=results.p

    passme=PassMe(user,passwd)

    if(results.a!=None):
        passme.check(results.a)
    else:
        passme.checkAll()
