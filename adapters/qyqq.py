# -*- coding: utf-8 -*-
from .adapter import Adapter
import re
import time

class Qyqq(Adapter):

    def __init__(self):
        super(Qyqq,self).__init__()
        self.auth_url='https://exmail.qq.com/cgi-bin/login'
        self.name='Qyqq'

    def check(self,user,passwd):

        return self.skip("Not finished yet")


        self.logger.info("Check password for  "+self.auth_url)

        starttime='1475204205079'
        # TODO parse from a username
        uin='lvxx@dxy.cn'
        domain='dxy.cn'
        # TODO make password
        p='h76j6bHu6fbPCTwCmGpykrzZh/ZXGOJ16yBhDKXUYycQysaSGRyGnoE9Fv0zsb587L6/+idXqJ/PewRydXCSxs8waXoI4naDgrVueZlojrr8oFabKSvQXmzUM9jRMEq0x9IwwE/sOOlsQqPTw1moofowtpHnjMxz9W+FuZTB4AA='
        # TODO what is this ?
        ts='1475204202'

        # params
        post={}
        post["firstlogin"]="false"
        post["domain"]=domain
        post["logindomain"]=domain
        post["aliastype"]="other"
        post["errtemplate"]="logindomain"
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
        post["loginentry"]=1
        post["dmtype"]=""
        post["fun"]=""
        post["pp"]=0000000
        post["verifycode"]=""
        post["ss"]=1

        # get url and cookie
        cookie='0.8355157954093462; _ga=GA1.2.886001592.1464193721; pac_uid=1_1252804799; eas_sid=2154l6H739R8Y1l8Z6u0Q780U8; tvfe_boss_uuid=adeb32746983dd9c; Hm_lvt_bdfb0d7298c0c5a5a2475c291ac7aca2=1473479638,1474278417,1474854394,1474949643; _ga=GA1.3.886001592.1464193721; pgv_pvid=2589071806; o_cookie=1252804799; pgv_info=ssid=s5339480576; ptui_loginuin=1252804799; ptcz=d27bde3413f133464a25cc8aa75f37ddf6447ee04eaaaf85c3293abe29c3d4c0; pt2gguin=o1252804799; uin=o1252804799; skey=@VgZkbizpW; ptisp=ctc; dm_login_weixin_scan=; qm_flag=2; qqmail_alias=lvxx@dxy.cn; biz_username=2612320504; CCSHOW=0000; qm_sk=-1682646792&RofTj-MZ; qm_ssum=-1682646792&65b375878fa46a5f9e0cebb2d3e04c5d; tinfo=EXPIRED; qm_authimgs_id=1; qm_verifyimagesession=h01d6abfaf9dd518722efb1aae6f6166b6421de80972546fc75678fc39f5e9c2664e214acf6d75aa384; ssl_edition=mail.qq.com'
        r=self.post(post,{'cookie':cookie})
        # use cookie access this url
        # check status
        url_p=re.compile(r' urlHead \+ "(.*?)";')
        target_p=re.compile(r'targetUrl\+="(.*?)"')
        matches=url_p.search(r.text)
        target_matches=target_p.search(r.text)
        url=matches.group(1)
        target_url=target_matches.group(1)

        redirect_url="https://exmail.qq.com/cgi-bin/"+url+target_url
        r=self.get(redirect_url,{cookie:cookie})

        checked_status=[-1,'found']
        # self.estimate(checked_status)
        return checked_status
