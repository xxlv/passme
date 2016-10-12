
from .adapter import Adapter
import re
# TODO
class Amazon(Adapter):

    def __init__(self):
        super(Amazon,self).__init__()
        self.name='Amazon'
        self.auth_url='https://www.amazon.cn/ap/signin'

    def check(self,user,passwd):

        return self.skip(" Not finished yet")
        self.logger.info("Check password for  "+self.auth_url)

        post={}
        post["appActionToken"]="b9Pyraq5Hj2F0frzFJ3IilsoI88tgj3D"
        post["appAction"]='SIGNIN'
        post["openid.pape.max_auth_age"]='ape:MA=='
        post["openid.return_to:"]='ape:aHR0cHM6Ly93d3cuYW1hem9uLmNuL2dwL3lvdXJzdG9yZS9jYXJkP2llPVVURjgmcmVmXz1jdXN0X3JlY19pbnRlc3RpdGlhbF9zaWduaW4='
        post["prevRID"]='ape:VFZDSjgwWlZDQ1lXVlFNRzFGUDY='
        post["openid.identity"]='ape:aHR0cDovL3NwZWNzLm9wZW5pZC5uZXQvYXV0aC8yLjAvaWRlbnRpZmllcl9zZWxlY3Q='
        post["openid.assoc_handle"]='SIGNIN'
        post["appAction"]='ape:Y25mbGV4'
        post["openid.mode"]='ape:Y2hlY2tpZF9zZXR1cA=='
        post["openid.ns.pape"]='ape:aHR0cDovL3NwZWNzLm9wZW5pZC5uZXQvZXh0ZW5zaW9ucy9wYXBlLzEuMA=='
        post["openid.claimed_id"]='ape:aHR0cDovL3NwZWNzLm9wZW5pZC5uZXQvYXV0aC8yLjAvaWRlbnRpZmllcl9zZWxlY3Q='
        post["pageId"]='ape:Y25mbGV4'
        post["openid.ns"]='ape:aHR0cDovL3NwZWNzLm9wZW5pZC5uZXQvYXV0aC8yLjA='
        post["email"]=''
        post["create"]='0'
        post["password"]=''
        post["metadata1"]='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'

        # sess=self.initSession()
        # cookie=sess.get('cookie','')
        cookie='x-wl-uid=1ba5ky4SRnPvgYfA1hYq2x3oc0X34F1iSGAAUNnJFR3MXveitYZhrcRFURXBeUdRer7l7xCvlZdk=; session-id-time=2082729601l; session-id=456-2033330-5537527; ubid-acbcn=452-1341976-0674006; session-token="xtJ7kyW/FLtz/nK5Fv7D1c8YeFROW1POZe8TSMS0yZb+rAvd/8kZIvSoaXbLjN51hvat981oyvU/vDfzZ3vctLEy9rd3/kuQXJpdi5bsxTzaBfhMCS+xJ7f2KO+Y64iIktTB/CmjZpCpOIGSMiz7v3RiqIk1GFoEgHjYfbNRRNdknZqZ2lNLpGKLYUYphwul1S/PZTuTXTHVijOg8Mnm6Q=="; csm-hit=TVCJ80ZVCCYWVQMG1FP6+s-TVCJ80ZVCCYWVQMG1FP6|1475650183635'

        r=self.post(post,headers={"cookie":cookie})

        headers=r.headers
        r=self.get(url="https://www.amazon.cn",headers={"cookie":cookie})



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
