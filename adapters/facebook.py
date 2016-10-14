
from .adapter import Adapter
import re

class Facebook(Adapter):

    def __init__(self):
        super(Facebook,self).__init__()
        self.name='Facebook'
        self.auth_url='https://www.facebook.com/login.php'



    def check(self,user,passwd):

        self.logger.info("Check password for  "+self.auth_url)

        # params
        post={}
        post["lsd"]=""
        post["email"]=user
        post["pass"]=passwd
        post["persistent"]=""
        post["default_persistent"]=""
        post["timezone"]=""
        post["lgndim"]=""
        post["lgnrnd"]=""
        post["lgnjs"]=""
        post["ab_test_data"]=""
        post["locale"]=""
        post["next"]=""
        post["qsstamp"]=""



        sess=self.initSession()
        cookie=sess.get('cookie','')
        r=self.post(post,headers={"cookie":cookie})
        headers=r.headers

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


        timezone_pattern=re.compile(r'name="timezone"\svalue="(.*?)"')
        lgndim_pattern=re.compile(r'name="lgndim"\svalue="(.*?)"')
        lgnrnd_pattern=re.compile(r'name="lgnrnd"\svalue="(.*?)"')
        lgnjs_pattern=re.compile(r'name="lgnjs"\svalue="(.*?)"')
        ab_test_data_pattern=re.compile(r'name="ab_test_data"\svalue="(.*?)"')
        locale_pattern=re.compile(r'name="locale"\svalue="(.*?)"')
        next_pattern=re.compile(r'name="next"\svalue="(.*?)"')
        qsstamp_pattern=re.compile(r'name="qsstamp"\svalue="(.*?)"')

        timezone_match=timezone_pattern.search(t)
        lgndim_match=lgndim_pattern.search(t)
        lgnrnd_match=lgnrnd_pattern.search(t)
        lgnjs_match=lgnjs_pattern.search(t)
        ab_test_data_match=ab_test_data_pattern.search(t)
        locale_match=locale_pattern.search(t)
        next_match=next_pattern.search(t)
        qsstamp_match=qsstamp_pattern.search(t)


        cookies="; ".join([str(x)+"="+str(y) for x,y in cookies.items()])
        sess={}
        if timezone_match is not None:
            sess['timezone']=timezone_match.group(1)
        else:
            sess['timezone']=''

        if lgndim_match is not None:
            sess['lgndim']=lgndim_match.group(1)
        else:
            sess['lgndim']=''

        if lgnrnd_match is not None:
            sess['lgnrnd']=lgnrnd_match.group(1)
        else:
            sess['lgnrnd']=''

        if  ab_test_data_match  is not None:
            sess['ab_test_data']=ab_test_data_match.group(1)
        else:
            sess['ab_test_data']=''

        if locale_match  is not None:
            sess['locale']=locale_match.group(1)
        else:
            sess['locale']=''

        if next_match is not None:
            sess['next']=next_match.group(1)
        else:
            sess['next']=''

        if qsstamp_match is not None:
            sess['qsstamp']=qsstamp_match.group(1)
        else:
            sess['qsstamp']=''

        return sess
