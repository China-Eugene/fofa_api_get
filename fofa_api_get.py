#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: Eugene

import requests
import base64
import json

#------------------------------基本配置区------------------------------

#Fofa基本认证信息
fofa_email = ""
fofa_key = ""
#搜索语句
fofa_search = ''
#搜索页数，和条数
page = "1"
size = "100"

##------------------------------函数执行区------------------------------
def API():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "*/*",
        "Connection": "close"
    }
    #搜索转码
    base_fofa_search = base64.b64encode(fofa_search.encode('utf-8')).decode("utf-8")
    #拼接FOFA_API请求URL
    fofa_search_url = 'https://fofa.so/api/v1/search/all?email={}&key={}&qbase64={}&page={}&size={}'.format(fofa_email, fofa_key, base_fofa_search, page, size)
    #发送API请求
    try:
        response = requests.get(fofa_search_url, headers=headers,verify=False, timeout=30)
    except Exception as e:
        print(e)
        print('\n'"检查一下fofa，或者是系统代理")
    else:
        #拿API中的URL
        print('\n')
        with open('url.txt',"a") as f: #把URL以txt的格式保存在同一目录下
	        dic=json.loads(response.text)
	        if 'results' in dic:
	            for i in dic['results']:
	                print(i[0]) #在终端输出URL
	                f.write(i[0]+'\n')
	            return dic
	        elif 'errmsg' in dic:
	            print(dic['errmsg'])
                
#------------------------------最终执行区------------------------------

if __name__ == '__main__':
    API()