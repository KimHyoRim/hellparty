#!/usr/bin/python
# coding=utf-8

import sys
import time
import sqlite3
import telepot
from pprint import pprint
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from datetime import date, datetime, timedelta
import traceback

import dsnoti_


def replyAptData(date_param, user):
    print(user, date_param)
    res_list = dsnoti_.getData(date_param)
    print(res_list)
    msg = ''
    for r in res_list:
        print( str(datetime.now()).split('.')[0], r )
        if len(r+msg)+1>dsnoti_.MAX_MSG_LENGTH:
            dsnoti_.sendMessage( user, msg )
            msg = r+'\n'
        else:
            msg += r+'\n'
    if msg:
        dsnoti_.sendMessage( user, msg )
    else:
        dsnoti_.sendMessage( user, '%s 기간에 해당하는 데이터가 없습니다.'%date_param )

def save( user, loc_param ):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users( user TEXT, location TEXT, PRIMARY KEY(user, location) )')
    try:
        cursor.execute('INSERT INTO users(user, location) VALUES ("%s", "%s")' % (user, loc_param))
    except sqlite3.IntegrityError:
        dsnoti_.sendMessage( user, '이미 해당 정보가 저장되어 있습니다.' )
        return
    else:
        dsnoti_.sendMessage( user, '저장되었습니다.' )
        conn.commit()

def check( user ):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users( user TEXT, location TEXT, PRIMARY KEY(user, location) )')
    cursor.execute('SELECT * from users WHERE user="%s"' % user)
    for data in cursor.fetchall():
        row = 'id:' + str(data[0]) + ', location:' + data[1]
        dsnoti_.sendMessage( user, row )


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type != 'text':
        dsnoti_.sendMessage(chat_id, '난 텍스트 이외의 메시지는 처리하지 못해요.')
        return

    text = msg['text']
    args = text

    print('try to ', args)
    replyAptData(args, chat_id)
    # if text.startswith('거래') and len(args) > 1:
    #     print('try to 거래', args[1])
    #     replyAptData(args[1], chat_id, args[2] )
    # elif text.startswith('지역') and len(args)>1:
    #     print('try to 지역', args[1])
    #     replyAptData( '201705', chat_id, args[1] )
    # elif text.startswith('저장')  and len(args)>1:
    #     print('try to 저장', args[1])
    #     save( chat_id, args[1] )
    # elif text.startswith('확인'):
    #     print('try to 확인')
    #     check( chat_id )
    # else:
    #     dsnoti_.sendMessage(chat_id, '모르는 명령어입니다.\n지역 [지역번호], 저장 [지역번호], 확인 중 하나의 명령을 입력하세요.')


today = date.today()
current_month = today.strftime('%Y%m')

print( '[',today,']received token :', dsnoti_.TOKEN )

bot = telepot.Bot(dsnoti_.TOKEN)
pprint( bot.getMe() )

bot.message_loop(handle)

print('Listening...')

while 1:
  time.sleep(10)