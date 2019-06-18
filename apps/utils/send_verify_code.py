# -*- coding: utf-8 -*-
import json
import requests


class SendVerifyCode(object):
    """
    发送验证码
    api_key：云片官网申请得到api_key
    """
    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"

    def send_msg(self, code, mobile):
        params = {
            "apikey": self.api_key,
            "mobile": mobile,
            "text": "【Rt生鲜】您的验证码是{code}。如非本人操作，请忽略本短信".format(code=code)
        }

        response = requests.post(self.single_send_url, data=params)
        re_dict = json.loads(response.text)
        return re_dict


if __name__ == '__main__':
    operation = SendVerifyCode("")
    operation.send_msg("", "")
