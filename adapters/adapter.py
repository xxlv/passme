# -*- coding: utf-8 -*-

import logging
import requests
import coloredlogs



class Adapter():

    def __init__(self):
        self.auth_url=''
        self._init_logger()

    def check(self,user,passwd):
        checked_status=[0,'nothing happend']
        self.estimate(checked_status)
        self.logger.debug('checking user %s  password is %s ' % (user,passwd))
        return checked_status

    def estimate(self,checked_status):
        if checked_status[0]==0:
            self.logger.warn(checked_status[1])
        if checked_status[0]==-1:
            self.logger.info(checked_status[1])

    def post(self,post,url=False,headers={}):
        if (url==False):
            url=self.auth_url

        sess=requests.Session()

        self.logger.debug('prepare request(post) url %s' % url)
        return sess.post(url,data=post,headers=headers)

    def get(self,url=False,headers={}):
        if (url==False):
            url=self.auth_url

        self.logger.debug('prepare get url %s' % url)
        sess=requests.Session()
        return sess.get(url,headers=headers)


    def _init_logger(self):

        coloredlogs.install()
        logging.getLogger("requests").setLevel(logging.WARNING)

        # logging.basicConfig(level=logging.INFO,format='%(asctime)s %(name)s[%(process)d] %(levelname)s %(message)s')
        logger = logging.getLogger('passme')
        logger.setLevel(logging.DEBUG)
        self.logger=logger
