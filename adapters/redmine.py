
from adapter import Adapter
import re

"""
    Redmine adapter for passme
    You should set auth_url first
"""

class Redmine(Adapter):

    def __init__(self):
        super(Redmine,self).__init__()
        # TODO set auth url
        self.name='Redmine'
        self.auth_url=None

    def check(self,user,passwd):

        if self.auth_url is None:
            return self.skip()

        self.logger.info("Check password for  "+self.auth_url)

        # params
        post={}
        post["utf8"]='✓'
        post["username"]=user
        post["password"]=passwd
        post["autologin"]=1

        sess=self.initSession()
        cookie=sess.get('cookie','')
        post["authenticity_token"]=sess.get('authenticity_token','')

        r=self.post(post,headers={"cookie":cookie})
        t=r.text

        partten=re.compile(r'/my/page')
        matches=partten.search(t)

        if(matches is not None):
            checked_status=[0,'Found redmine user ('+user+') using this password']
        else:
            checked_status=[-1,'redmine not found user use this pwd']

        self.estimate(checked_status)
        return checked_status


    def initSession(self):

        url=self.auth_url
        r=self.get(url)

        cookies=r.cookies
        t=r.text
        pattern=re.compile(r'name="authenticity_token"\stype="hidden"\svalue="(.*?)"')
        match=pattern.search(t)

        if match is not None:
            authenticity_token=match.group(1)
        else:
            authenticity_token=''
        cookies="; ".join([str(x)+"="+str(y) for x,y in cookies.items()])

        return {"authenticity_token":authenticity_token,"cookie":cookies}
