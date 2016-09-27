# -*- coding: utf-8 -*-


import logging
import requests


class Adapter():

    def __init__(self):
        self.auth_url=''
        self._init_logger()

    def check(self,user,passwd):
        checked_status=[0,'nothing happend']
        self.estimate(checked_status)
        return checked_status

    def estimate(self,checked_status):
        if checked_status[0]==0:
            self.logger.info(checked_status[1])
        if checked_status[0]==-1:
            self.logger.error(checked_status[1])

    def postWithFormData(self,post):
        return requests.post(self.auth_url,data=post)


    def _init_logger(self):

        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger("passme")
        logger.setLevel(logging.DEBUG)
        # # create console handler and set level to debug
        # ch = logging.StreamHandler()
        # ch.setLevel(logging.DEBUG)
        # # create formatter
        # formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        # # add formatter to ch
        # ch.setFormatter(formatter)
        # # add ch to logger
        # logger.addHandler(ch)
        self.logger=logger
