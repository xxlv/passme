
from adapter import Adapter
import re

class Meituan(Adapter):

    def __init__(self):
        super(Meituan,self).__init__()
        self.name='Meituan'
        self.auth_url='http://passport.meituan.com/account/unitivelogin'


    def check(self,user,passwd):
        self.logger.info("Check password for " + self.auth_url)

        post={}
        post["email"]=user
        post["password"]=passwd
        post["captcha"]=''
        post["origin"]='account-login'
        post["password"]='r2b6mk7v-0XVvoPC4LkaQuYQeE7RqcMWmjkA'

        sess=self.initSession()
        cookie=sess.get('cookie','')

        post["fingerprint"]=sess.get('finger')
        post["csrf"]=sess.get('csrf')

        r=self.post(post,headers={"cookie":cookie})
        headers=r.headers
        captcha_pattern=re.compile(r'https://passport.meituan.com/account/captcha')
        matches=captcha_pattern.search(r.text)
        if matches is not None:
            return self.skip("Sorry "+self.auth_url + ' Need captcha..')

        if(False):
            self.found(user,passwd)
        else:
            self.not_found(user,passwd)

        return



    def initSession(self):

        url=self.auth_url
        r=self.get(url)
        cookies=r.cookies
        t=r.text
        fingerprint_pattern=re.compile(r'type="hidden"\sname="fingerprint"\sclass="J-fingerprint"\svalue="(.*?)"')
        csrf_pattern=re.compile(r'type="hidden"\sname="csrf"\svalue="(.*?)"')

        finger_match=fingerprint_pattern.search(t)
        csrf_match=csrf_pattern.search(t)
        finger=finger_match.group(1)
        csrf=csrf_match.group(1)
        if finger is None:
            finger="0-16-1-"

        cookies="; ".join([str(x)+"="+str(y) for x,y in cookies.items()])

        return {"cookie":cookies,"csrf":csrf,"finger":finger}
