# -*- coding: utf-8 -*-

import sys
import os
import argparse

import importlib
from os import listdir
from os.path import isfile

# adapter list
sys.path.append('./adapters')
from adapters import *


class PassMe:

    def __init__(self,user,passwd):
        self.user=user
        self.passwd=passwd
        self.adapter_path='./adapters'
        self._init_adapters()


    def check(self,adapter_name):
        for adapter in self.adapters:
            if adapter.upper()==adapter_name.upper():
                adapter=self._class_for_name('adapters',adapter)
                if adapter is not None:
                    adapter=adapter()
                    adapter.check(self.user,self.passwd)


    def checkAll(self):
        result =list()
        for adapter in self.adapters:
            adapter=self._class_for_name('adapters',adapter)
            if adapter is not None:
                adapter=adapter()
                checked_status=adapter.check(self.user,self.passwd)
                result.append(checked_status)

        return result


    def listAllAdapters(self):
        for adapter in self.adapters:
            print(adapter+"\n")


    def _init_adapters(self):
        self.adapters=[]

        files=listdir(self.adapter_path)

        for f in files:
            f=os.path.splitext(f)
            adaper_name=f[0].capitalize()
            if(adaper_name[0]!='_' and adaper_name!='Adapter'):
                self.adapters.append(adaper_name)

    def _class_for_name(self,module_name,class_name):

        m=importlib.import_module(module_name)
        c=getattr(m,class_name)
        return c

if __name__=='__main__':

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
