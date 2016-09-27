# -*- coding: utf-8 -*-

from adapter import Adapter

import time

class Qyqq(Adapter):
    
    def __init__(self):
        super(Qyqq,self).__init__()
        self.auth_url='https://exmail.qq.com/cgi-bin/login'


    def check(self,user,passwd):

        self.logger.info("Check pass for  "+self.auth_url)

        starttime=int(1000*time.time())
        # TODO parse from a username
        uin='lvxx'
        domain='dxy.cn'
        # TODO make password
        p=''
        # TODO what is this ?
        ts='1474949642'
        inputuin='lvxx@dxy.cn'

        # params
        post={}
        post["firstlogin"]="false"
        post["domain"]=domain
        post["aliastype"]="other"
        post["errtemplate"]="dm_loginpage"
        post["first_step"]=""
        post["buy_amount"]=""
        post["year"]=""
        post["company_name"]=""
        post["sis_get_dp_couponid"]=""
        post["source"]=""
        post["qy_code"]=""
        post["starttime"]=starttime
        post["redirecturl"]=""
        post["f"]="biz"
        post["uin"]=uin
        post["p"]=p
        post["delegate_url"]=""
        post["ts"]=ts
        post["from"]=""
        post["ppp"]=""
        post["chg"]=0
        post["loginentry"]=3
        post["dmtype"]=""
        post["fun"]=""
        post["inputuin"]=inputuin
        post["verifycode"]=""
        post["ss"]=1

        r=self.post(post)

        text=r.text
        # TODO
        # get url and cookie
        # use cookie access this url
        # check status

        checked_status=[0,'']
        self.estimate(checked_status)

        return checked_status
