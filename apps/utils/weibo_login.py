# -*- coding: utf-8 -*-
import requests


def get_auth_url():
    weibo_auth_url = "https://api.weibo.com/oauth2/authorize"
    redirect_url = "http://127.0.0.1:8000/complate/weibo/"
    auth_url = weibo_auth_url+"?client_id={0}&redirect_uri={1}".format("386808437", redirect_url)
    print(auth_url)


if __name__ == '__main__':
    get_auth_url()

