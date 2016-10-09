
from adapter import Adapter
import re
import json

class Zhihu(Adapter):

    def __init__(self):
        super(Zhihu,self).__init__()
        self.name='Zhihu'
        self.auth_url='https://www.zhihu.com/login/email'
        self.auth_url_phone='https://www.zhihu.com/login/phone_num'


    def check(self,user,passwd):

        self.logger.info("Check password for  "+self.auth_url)

        # params
        post={}
        post["email"]=user
        post["password"]=passwd
        post["captcha_type"]='cn'
        post["remember_me"]='true'

        sess=self.initSession()

        cookie=sess.get('cookie','')
        post["_xsrf"]=sess.get('xsrf','')

        headers={
            "accept": "application/json",
            "accept-encoding":"gzip, deflate",
            "accept-language": "en-US,en;q=0.8",
            "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
            "Host":"www.zhihu.com",
            "Origin":"https://www.zhihu.com",
            "Referer":"https://www.zhihu.com/",
            "X-Xsrftoken":post['_xsrf'],
            "cookie":cookie
        }
        r=self.post(post,headers=headers)
        response=json.loads(r.text)

        if(response.get('captcha',None) is None):
            return self.skip(self.auth_url+' Need captcha')

        if(response.get('r')==0):
            self.found(user,passwd)
        else:
            self.not_found(user,passwd)
        return


    def initSession(self):

        url="https://www.zhihu.com/"
        headers={
            "accept": "application/json",
            "accept-encoding":"gzip, deflate",
            "accept-language": "en-US,en;q=0.8",
            "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
            "Host":"www.zhihu.com"
        }

        r=self.get(url,headers=headers)
        cookies=r.cookies
        t=r.text

        pattern=re.compile(r'name="_xsrf"\svalue="(.*?)"')
        match=pattern.search(t)

        if match is not None:
            xsrf=match.group(1)
        else:
            xsrf=''

        cookies="; ".join([str(x)+"="+str(y) for x,y in cookies.items()])
        return {"xsrf":xsrf,"cookie":cookies}
