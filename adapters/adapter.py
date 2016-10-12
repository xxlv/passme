# -*- coding: utf-8 -*-

import logging
import requests
import coloredlogs



class Adapter():

    def __init__(self):
        self.auth_url=''
        self._init_logger()
        self.name='Adapter'
        self.session=None

    def check(self,user,passwd):
        checked_status=[0,'nothing happend']
        self.estimate(checked_status)
        self.logger.debug('checking user %s  password is %s ' % (user,passwd))
        return checked_status

    def estimate(self,checked_status):
        if checked_status[0]==0:
            pass
        if checked_status[0]==-1:
            pass


    def skip(self,reason=''):

        skip="Oppps -_-Skip "+self.name
        if reason is not '':
            skip+=" Reason: "+ reason

        self.logger.warn(skip)
        return

    def skilAll(self):
        self.logger.warn("Skip All")
        return



    def found(self,user='',passwd=''):

        # TODO  FOUND USER USE THIS PASSWORD
        self.logger.error(self.name +" FOUND user "+ str(user) +" use this password")
        return


    def not_found(self,user='',passwd=''):
        # TODO NOT FOUND USER USE THIS PASSWORD
        self.logger.info(self.name +" NOT FOUND user "+str(user) +" use this password")
        return


    def post(self,post,headers={},url=False):

        if (url==False):
            url=self.auth_url

        sess=self._get_session()

        self.logger.debug('prepare request(post) url %s' % url)
        return sess.post(url,data=post,headers=headers)

    def get(self,url=False,headers={}):
        if (url==False):
            url=self.auth_url

        self.logger.debug('prepare get url %s' % url)

        sess=self._get_session()
        r= sess.get(url,headers=headers)
        r.connection.close()
        return r


    def _get_session(self):
        if(self.session is None):
            self.session=requests.Session()
        return self.session


    def _init_logger(self):
        coloredlogs.install()
        logging.getLogger("requests").setLevel(logging.WARNING)
        logger = logging.getLogger('passme')
        logger.setLevel(logging.INFO)
        self.logger=logger
