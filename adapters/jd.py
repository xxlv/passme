
from adapter import Adapter
import re

# TODO

class Jd(Adapter):

    def __init__(self):
        super(Jd,self).__init__()
        self.name='Jd'
        self.auth_url='https://passport.jd.com/uc/loginService'

    def check(self,user,passwd):

        self.logger.info("Check password for "+ self.auth_url)

        sess=self.initSession()
        cookie=sess.get('cookie','')
        uuid=sess.get('uuid')
        eid=sess.get('eid')
        fp=sess.get('fp')
        _t=sess.get('t')
        loginType=''
        loginname=user
        nloginpwd='CMHAzI2hrWiGniufQhcVVBh14LYQlypcp9G9X0K3wj7LHfG/nhzhqd2mOCkMXmPbuX6Xyma49+UtpTGMoi+FnVC5C/fhSh4Q308VZEpQFkgUZR2EzCWJTHvoAIw5JaWIwAglGr3gM2NREQ/2GLy2kXHbd5NW5PDWSbBRxGDT4oY='
        chkRememberMe='on'
        authcode=''

        # params
        post={}
        post["uuid"]=uuid
        post["eid"]=eid
        post["fp"]=fp
        post["_t"]=_t
        post["loginType"]=loginType
        post["loginname"]=loginname
        post["nloginpwd"]=nloginpwd
        post["chkRememberMe"]=chkRememberMe
        post["authcode"]=authcode


        self.auth_url=self.auth_url+"?uuid="+uuid

        r=self.post(post,headers={"cookie":cookie})

        headers=r.headers

        # TODO

        logined=False


        if(logined):
            self.found(user,passwd)
            checked_status=[0,'Found '+self.name+' user ('+user+') using this pwd']
        else:
            self.not_found(user,passwd)
            checked_status=[-1,self.name+' not found user use this pwd']

        self.estimate(checked_status)

        return checked_status


    def initSession(self):

        session={}

        url='https://passport.jd.com/new/login.aspx'
        r=self.get(url)

        uuid_pattern=re.compile(r'type="hidden"\sid="uuid"\sname="uuid"\s*value="(.*?)"')
        eid_pattern=re.compile(r'type="hidden"\sname="eid"\sid="eid"\svalue="(.*?)"')
        fp_pattern=re.compile(r'type="hidden"\sname="fp"\sid="sessionId"\svalue="(.*?)"')
        t_pattern=re.compile(r'type="hidden"\sname="_t"\sid="token"\svalue="(.*?)"')
        pubkey_pattern=re.compile(r'type="hidden"\sname="pubKey"\sid="pubKey"\svalue="(.*?)"')
        jmkAdRazzi_pattern=re.compile(r'type="hidden"\sname="JmkAdRazzi"\sid="pubKey"\svalue="(.*?)"')

        text=r.text
        cookies=r.cookies
        cookies="; ".join([str(x)+"="+str(y) for x,y in cookies.items()])

        uuid_matches=uuid_pattern.search(text)
        eid_matches=eid_pattern.search(text)
        fp_matches=fp_pattern.search(text)
        t_matches=t_pattern.search(text)
        pubkey_matches=pubkey_pattern.search(text)
        jmkadrazzi_matches=jmkAdRazzi_pattern.search(text)


        if(uuid_matches):
            uuid=uuid_matches.group(1)
        else:
            uuid=''

        if(eid_matches):
            eid=eid_matches.group(1)
        else:
            eid=''

        if(fp_matches):
            fp=fp_matches.group(1)
        else:
            fp=''

        if(t_matches):
            t=t_matches.group(1)
        else:
            t=''

        if(pubkey_matches):
            pubkey=pubkey_matches.group(1)
        else:
            pubkey=''

        if(jmkadrazzi_matches):
            jm=jmkadrazzi_matches.group(1)
        else:
            jm=''

        session['uuid']=uuid
        session['eid']=eid
        session['fp']=fp
        session['t']=t
        session['pubkey']=pubkey
        session['jm']=jm
        session['cookie']=cookies

        return session
