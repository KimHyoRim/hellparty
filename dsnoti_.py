#!/usr/bin/python
# coding=utf-8

import sys
from urllib.request import urlopen
from urllib.parse import quote
import time
from xml.etree import ElementTree
import urllib.request
from xml.dom.minidom import parse, parseString
from urllib.request import urlopen
from urllib.parse import quote
import sqlite3
import telepot
from pprint import pprint
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from datetime import date, datetime, timedelta
import traceback

key = "475bf83ac2911d034998c841c40225c7"
TOKEN = '856816592:AAHDHTv27olsdjqmTv96DdXP2YBH49iYAxc'
MAX_MSG_LENGTH = 300
baseurl =  "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList" \
                    ".xml?key="+key
bot = telepot.Bot(TOKEN)

def getData( date_param):
    res_list = []
    url = baseurl+'&targetDt='+date_param
    print(url)
    req = urllib.request.Request(url)

    data = urllib.request.urlopen(req).read()
    tree = ElementTree.fromstring(data)

    itemElements = tree.getiterator("dailyBoxOffice")

    MmovieNm = []
    Mrank = []
    MshowRange = []
    MopenDt = []
    MaudiAcc = []
    MrankInten = []
    MsalesAcc = []
    Mimage = []

    for item in itemElements:

        movieNm = item.find("movieNm")
        rank = item.find("rank")
        openDt = item.find("openDt")
        audiAcc = item.find("audiAcc")  # 누적관객수
        salesAcc = item.find("salesAcc")  # 누적 매출

        MmovieNm.append(movieNm.text)
        Mrank.append(rank.text)
        MopenDt.append(openDt.text)
        MaudiAcc.append(audiAcc.text)
        MsalesAcc.append(salesAcc.text)
        try:
            for i in range(10):
                row = Mrank[i] + "등\n\n" \
                    + "영화 제목 : " + MmovieNm[i] + "\n\n" \
                    + "영화 개봉일 : " + MopenDt[i] + "\n\n" \
                    + "누적 매출액 : " + MsalesAcc[i] + "원\n\n" \
                    + "누적 관객수 : " + MaudiAcc[i] + "명\n\n"
        except IndexError:
            pass

        print(row)
        res_list.append(row)

    return res_list

def sendMessage(user, msg):
    try:
        bot.sendMessage(user, msg)
    except:
        traceback.print_exc(file=sys.stdout)

def run(date_param, param='11710'):
    conn = sqlite3.connect('logs.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS logs( user TEXT, log TEXT, PRIMARY KEY(user, log) )')
    conn.commit()

    user_cursor = sqlite3.connect('users.db').cursor()
    user_cursor.execute('CREATE TABLE IF NOT EXISTS users( user TEXT, location TEXT, PRIMARY KEY(user, location) )')
    user_cursor.execute('SELECT * from users')

    for data in user_cursor.fetchall():
        user = data[0]
        print(user, date_param)
        res_list = getData(date_param)
        msg = ''
        for r in res_list:
            try:
                cursor.execute('INSERT INTO logs (user,log) VALUES ("%s", "%s")'%(user,r))
            except sqlite3.IntegrityError:
                pass
            else:
                print( str(datetime.now()).split('.')[0], r )
                if len(r+msg)+1>MAX_MSG_LENGTH:
                    sendMessage( user, msg )
                    msg = r+'\n'
                else:
                    msg += r+'\n'
        if msg:
            sendMessage( user, msg )
    conn.commit()

if __name__=='__main__':
    today = date.today()
    current_month = today.strftime('%Y%m')

    print( '[',today,']received token :', TOKEN )

    pprint( bot.getMe() )

    run(current_month)