
from .adapter import Adapter
import re

class Gitlab(Adapter):

    def __init__(self):
        super(Gitlab,self).__init__()
        self.name='Gitlab'
        self.auth_url=None



    def check(self,user,passwd):

        if self.auth_url is None:
            return self.skip('Please set auth url first')

        self.logger.info("Check password for  "+self.auth_url)

        # params
        post={}
        post["utf8"]='✓'
        post["user[login]"]=user
        post["user[password]"]=passwd
        post["user[remember_me]"]=0

        sess=self.initSession()
        cookie=sess.get('cookie','')
        post["authenticity_token"]=sess.get('authenticity_token','')

        r=self.post(post,headers={"cookie":cookie})

        partten=re.compile(r'class="sign-out-link"')
        matches=partten.search(r.text)

        if(matches):
            self.found(user,passwd)
            checked_status=[0,'Found gitlab user ('+user+') using this pwd']

        else:
            self.not_found(user,passwd)
            checked_status=[-1,'Not found gitlab user ('+user+') using this pwd']


        self.estimate(checked_status)

        return checked_status


    def initSession(self):

        url=self.auth_url
        r=self.get(url)

        cookies=r.cookies
        t=r.text
        pattern=re.compile(r'type="hidden"\sname="authenticity_token"\svalue="(.*?)"')
        match=pattern.search(t)

        if match is not None:
            authenticity_token=match.group(1)
        else:
            authenticity_token=''


        cookies="; ".join([str(x)+"="+str(y) for x,y in cookies.items()])

        return {"authenticity_token":authenticity_token,"cookie":cookies}
