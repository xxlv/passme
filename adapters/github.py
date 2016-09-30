
from adapter import Adapter
import re

class Github(Adapter):

    def __init__(self):
        super(Github,self).__init__()
        self.name='Github'
        self.auth_url='https://github.com/session'



    def check(self,user,passwd):

        self.logger.info("Check password for  "+self.auth_url)

        # params
        post={}
        post["commit"]="Sign in"
        post["login"]=user
        post["password"]=passwd

        sess=self.initSession()
        cookie=sess.get('cookie','')
        post["authenticity_token"]=sess.get('authenticity_token','')

        r=self.post(post,headers={"cookie":cookie})
        headers=r.headers

        if(headers.get('X-GitHub-User','')!=''):
            checked_status=[0,'Found github user ('+user+') using this pwd']
            self.found(user,passwd)
        else:
            checked_status=[-1,'github not found user use this pwd']
            self.not_found(user,passwd)


        self.estimate(checked_status)

        return checked_status


    def initSession(self):

        url='https://github.com/login'
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
