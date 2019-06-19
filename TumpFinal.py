from tkinter import*

from tkinter.filedialog import *

from tkinter.simpledialog import*


import max
import tkinter.ttk
from PIL import Image, ImageTk
from tkinter import font
from io import BytesIO
import codecs
from urllib.request import urlopen
from urllib.parse import quote


from datetime import datetime
from xml.etree import ElementTree

import urllib.request
from xml.dom.minidom import parse, parseString
from urllib.request import urlopen
from urllib.parse import quote

import smtplib
from email.mime.text import MIMEText



client_id = "c2aiMTmEQXnK5nZxnwu9"
client_secret = "fYDB7FeEIY"


class test:
    #maildata =""
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.configure(background = "gray11")
        # self.label = tkinter.Label(self.window, background = "orange3")
        self.window.title("영화 정보 검색")
        self.window.geometry("875x800+100+0") # 800 500
        self.window.resizable(False, False)
        imageObj = PhotoImage(file = "image/lion.png")
        self.mainImage = Label(self.window, image=imageObj, background = "gray11")
        self.mainImage.place(x = 220, y = -23)
        self.maildata = ""

        self.menu = tkinter.ttk.Notebook(self.window, width = 875, height = 700)
        self.menu.place(x=0, y=210)

        self.Search_Button_Action()
        self.inputEmailText = ""

        #self.menu.pack()

        # 1번째 프레임
        self.frame1 = tkinter.Frame(self.window, background = "gray11")
        self.menu.add(self.frame1, text="페이지1")
        # self.TextImage = PhotoImage(file="goldmetal.png")
        self.text1 = tkinter.Text(self.frame1, width=45, height=41, background="DarkGoldenrod3")
        # self.text1.image_create('0.0', image=self.TextImage)
        self.text1.place(x=12, y=12)



        self.text1.insert(INSERT, "<< " + str(self.now.year) + "년 " + str(self.now.month) + "월 " + str(self.now.day) + "일 " + "박스오피스 순위 >>")
        self.text1.insert(INSERT, "\n\n")


        ######################c++/c연동############################
        self.cmax = []

        for i in range(10):
            self.cmax.append(int(max.accsales(self.MaudiAcc[i])))

        self.result = 0
        self.max_i = 0

        for i in range(10):
            if self.cmax[i] > self.result:
                self.result = self.cmax[i]
                self.max_i = i

        self.text1.insert(INSERT, "최다 관객 동원 영화 : "+self.MmovieNm[self.max_i]+"\n\n")
        self.text1.insert(INSERT, "누적 관객 수 : "+self.MaudiAcc[self.max_i]+"명\n\n")
        ######################################################################33

        for i in range(10):# range(len(self.Mimage)):   # range(10):
            self.text1.insert(INSERT, "<<" + self.Mrank[i]+"등>>")
            self.text1.insert(INSERT, "\n\n")

            self.text1.insert(INSERT, "영화 제목 : ")
            self.text1.insert(INSERT, self.MmovieNm[i])
            self.text1.insert(INSERT, "\n\n")

            self.text1.insert(INSERT, "개봉 일자 : ")
            self.text1.insert(INSERT, self.MopenDt[i])
            self.text1.insert(INSERT, "\n\n")

            self.text1.insert(INSERT, "누적 관객수 : ")
            self.text1.insert(INSERT, self.MaudiAcc[i]+"명")
            self.text1.insert(INSERT, "\n\n")

            self.text1.insert(INSERT, "누적 매출액 : ")
            self.text1.insert(INSERT, self.MsalesAcc[i] + "원")
            self.text1.insert(INSERT, "\n\n")

            self.text1.insert(INSERT, "전날대비 순위 변동 : ")
            self.text1.insert(INSERT, self.MrankInten[i])
            self.text1.insert(INSERT, "\n\n\n")


            if self.Mimage[i] is not None:
                u = urlopen(self.Mimage[i])
                r_data = u.read()
                u.close()

                if Image.open(BytesIO(r_data)):
                    im = Image.open(BytesIO(r_data))
                photo = ImageTk.PhotoImage(im)
                self.labelImage1 = Label(image=photo, background = "gray11")
                self.labelImage1.image = photo
                self.labelImage1.place(x=350 + 130 * (i % 4), y=243 + 185 * (i // 4)) # (x=320 + 110 * (i % 4), y=130 + 185 * (i // 4))
                TempFont = font.Font(self.frame1, size=8, weight='bold', family='D2 Coding')  # 폰트를 만든다.

                t = self.MmovieNm[i].split(':')
                if len(t[0]) > 6:
                    boxoffice_n = Label(font=TempFont, text=str(i + 1) + "등 - " + t[0], background="gray11",
                                        foreground="DarkGoldenrod3")
                    boxoffice_n.place(x=357 + 126 * (i % 4), y=403 + 185 * (i // 4))
                else:
                    boxoffice_n = Label(font=TempFont, text=str(i + 1) + "등 - " + t[0], background="gray11",
                                        foreground="DarkGoldenrod3")
                    boxoffice_n.place(x=376 + 126 * (i % 4), y=403 + 185 * (i // 4))

            # else:
           #      nonephoto = PhotoImage(file="no.png")
            #     nonelabel = Label(image=nonephoto)
            #     nonelabel.image = nonephoto
             #    nonelabel.place(x = 0, y = 0) # (x=320 + 110 * (i % 4), y=130 + 185 * (i // 4))
            self.text1.insert(INSERT, "\n\n\n")

        # 2번쨰 프레임
        self.frame2 = tkinter.Frame(self.window, background="gray11")
        self.menu.add(self.frame2, text="페이지2")
        # self.menu.configure(background = "red")

        self.searchEntry2 = tkinter.Entry(self.frame2, borderwidth=12, relief="raised", background="DarkGoldenrod3")
        # self.searchEntry2.pack(anchor="n", side="left")
        self.searchEntry2.pack()
        self.searchEntry2.place(x=10, y=50)

        self.button2Image = PhotoImage(file="image/lionButton.png")
        self.button2 = tkinter.Button(self.frame2, image=self.button2Image, width=45, height=40, text="버튼 2",
                                      command=self.buttonComm2, background="gray11", bd="0")
        # self.button2.pack(anchor="n", side="left")
        self.button2.pack()
        self.button2.place(x=175, y=47)

        self.scrollbar2 = tkinter.Scrollbar(self.frame2)
        # self.scrollbar2.pack()
        # self.scrollbar2.place(x=210,y=50)

        self.frameImage = PhotoImage(file="image/frameImage.png")
        self.frameLabel2 = tkinter.Label(self.frame2, image=self.frameImage, width=600, height=510, background="gray11")
        self.frameLabel2.pack()
        self.frameLabel2.place(x=240, y=30)

        self.text2 = tkinter.Text(self.frame2, width=63, height=30, yscrollcommand=self.scrollbar2.set,
                                  background="DarkGoldenrod3")
        # f.text2.insert(INSERT, '장수현 최고')
        self.text2.place(x=320, y=90)

        self.scrollbar2.config(command=self.text2.yview)
        # self.scrollbar2.pack(side="right", fill="y")






        # 3번째 프레임
        self.frame3 = tkinter.Frame(self.window, background = "gray11")
        self.menu.add(self.frame3, text="페이지3")
        self.canvasImage = PhotoImage(file="image/ubdGraphImage.png")
        self.canvasButton = tkinter.Button(self.frame3, width = 830, height = 495, image = self.canvasImage, command = self.buttonComm3, state = "active", bd = "0")
        self.canvas = tkinter.Canvas(self.frame3, width=830, height=495, bd=2, background = "gray11")
        self.canvasButton.pack()
        # self.canvas.pack()
        # self.canvas.place(x=20, y=20)

        self.x = 200
        self.y = 495
        self.barW = (self.x - 32) / 2
        for i in range(10):
            self.ubd = []
            self.ubd.append(int(self.MaudiAcc[i])//172213)
            # self.ubdFloat = []
            # self.ubdFloat.append((round(int(self.MaudiAcc[i])/172213),2))
            # self.ubdFloat.append(format(int(self.MaudiAcc[i]) / 172213), '.2f')

            self.canvas.create_rectangle(10 + self.barW * (i), (self.y - 20) - (int(self.MaudiAcc[i]) // 20000), 35 + self.barW * (i), self.y - 20, fill = "DarkGoldenrod3")
            self.canvas.create_text(35 + self.barW * i, self.y - 5, text=str(self.ubd)+" UBD", fill = "DarkGoldenrod3")
            self.canvas.create_rectangle(10 + self.barW * (i) + 25, (self.y - 20) - (172213 // 20000), 35 + self.barW * (i) + 25, self.y - 20, fill = "DarkOrange4")

            # if int(self.MaudiAcc[i])/172213 >= 1:
            #     self.canvas.create_rectangle(10 + self.barW * (i), (self.y-20) - (int(self.MaudiAcc[i]) // 20000), 35 + self.barW * (i), self.y - 20)
            #     #self.canvas.create_text(35 + self.barW * i, self.y - 5, text=str(self.ubd)+" UBD")
            # else:
            #     self.canvas.create_rectangle(10 + self.barW * (i), (self.y - 20) - (int(self.MaudiAcc[i]) // 20000), 35 + self.barW * (i), self.y - 20)
            #     self.canvas.create_text(35 + self.barW * i, self.y - 5, text=str(int(self.MaudiAcc[i])/172213) + " UBD")
            # self.canvas.create_rectangle(10 + self.barW * (i) + 25, (self.y-20) - (172213//20000), 35 + self.barW * (i) + 25, self.y - 20)

            # 4번째 프레임
        self.frame4 = tkinter.Frame(self.window, background="gray11")
        self.menu.add(self.frame4, text="페이지4")

        self.TempFont = font.Font(self.frame4, size=15, weight='bold', family='Consolas')
        self.inputEmailText = Entry(self.frame4, font=self.TempFont, width=25, borderwidth=12, relief="raised", background="DarkGoldenrod3")
        self.inputEmailText.pack()
        self.inputEmailText.place(x=260, y=70)

        self.emailButtonImage = PhotoImage(file="image/lionButton.png")
        self.emailButton4 = Button(self.frame4, font=self.frame4, width=50, height=45, image=self.emailButtonImage, command=self.sendEmailButton, background="gray11", bd="0")
        self.emailButton4.pack()
        self.emailButton4.place(x=560, y=70)

        self.successButtonimage = PhotoImage(file="image/mailSend.png")
        self.emailSendButton4 = Button(self.frame4, width=270, height=50, image=self.successButtonimage, background="gray11", bd="0", )

        self.window.mainloop()

    def sendEmailButton(self):

        # 이메일
        self.smtp_gmail = smtplib.SMTP('smtp.gmail.com', 587)
        self.smtp_gmail.ehlo()
        self.smtp_gmail.starttls()
        self.smtp_gmail.login('erppp5o@gmail.com', 'tlqdldnjf12A')

        self.receiveMail = str(self.inputEmailText.get())

        self.realMailText = []
        for i in range(10):
            # self.realMailText.append("영화 순위 : "+str(i+1) + "위\n 영화 제목 : " + str(self.MmovieNm[i]) + "\n   ")
            self.maildata += "영화 순위 : " + str(i + 1) + "위" + str("\n") + "영화 제목 : " + str(self.MmovieNm[i]) + str(
                "\n\n\n")

        # print(self.realMailText)
        self.contents = self.maildata
        self.msg = MIMEText(self.contents, 'html', _charset='UTF-8')

        self.msg['Subject'] = "박스오피스 순위 정보 1~10"
        self.msg['From'] = 'erppp5o@gmail.com'
        # self.msg['To'] = 'erpppo@naver.com'
        self.msg['To'] = self.receiveMail
        # self.smtp_gmail.sendmail("erppp5o@gmail.com", "erpppo@naver.com", self.msg.as_string())
        self.smtp_gmail.sendmail("erppp5o@gmail.com", self.receiveMail, self.msg.as_string())

        self.smtp_gmail.quit()


        if self.maildata is not None:
            self.emailSendButton4.pack()
            self.emailSendButton4.place(x=300, y=200)

        self.maildata = ""

        #if self.maildata is None:
            #self.emailSendButton4.destroy()


    def buttonComm3(self):
        isphoto = False
        self.canvasButton.destroy()
        self.canvas.pack()

        for i in range(10):

            t = self.MmovieNm[i].split(':')
            # self.MovieNameText.pack()
            self.MovieNameTexti = tkinter.Text(self.frame3, width=11, height=3, background="gray11",
                                               foreground="DarkGoldenrod3", bd="0")
            self.MovieNameTexti.place(x=85 * (i) + 12, y=540)
            self.MovieNameTexti.insert(tkinter.CURRENT, " [" + t[0] +"]")
            # self.MovieNameTexti.tag_config("강조", )


    def buttonComm2(self):
        self.text2.delete("1.0", END)
        movie_str = urllib.parse.quote(self.searchEntry2.get())
        noneimage2 = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAG4AAACeCAMAAADkF8/QAAAAS1BMVEXp6el0dHTMzM' \
                     'yvr6+RkZHIyMi8vLz8/Pzm5ub////W1tbg4OCysrLd3d2srKygoKD09PSmpqaZmZnKysqDg4O/v7+Kiop7e3vw8PAN' \
                     'vY8LAAAF5UlEQVR4nO2ZCXOjOBCFhS5kHUji/v+/dF8LbMgkU7tZiPcovaqxCWT46NfdatlhrKqqqqqqqqqqqqqqqupfp' \
                     'ZTeSns83sdb28ejfaxvoqX20Qbbtu/hkZFWKfNo3wAjI5maOLfrG9JXjNTTwK0NP58+MlL5SSngrGl/1k4y0mihd1xYfzR' \
                     '9oLW26zRwQ8G59IPpIyN17Dxw4BUca3+Mlx6t62IngFPGkpvBGdj5I+VCRqq5z4TzASlEJwBn0o+kj+o/WZ17mOm9faD3gCP' \
                     'eT9iJtLUpoe65z5S89UHxFd796aP6xy3XFcAUJuE9x5mHIzsdyuXe9JGRDGEQmEI02msDXBtKubh7uw+xpQDbkCezhbii0xP' \
                     'xcMLB0Xu7L21l8QQiRItqQcgPQjJEmG61s20d2bYDSTjer60r0oeH2J7kFq1ta2nRImIRCC6E46f9/S7g+lgHZS0fFFReh+' \
                     '34o3j481v9JaUHli0hNJZKpSlQPpVwPwjrjL0UIFzchcbLfaeHYKzwqEfRd46ZkzZHubqIM6gO1MOagoydVtZxH+06yF4ObC' \
                     'tVQ5lkpTRX66/hUhmkKANm+xeOry7LGCgmqhCUpaM2hMJVHN/mNkzccRbRBWVRFg551N53nh84cT26rQf4EZ3Vo0osKPwEO4P' \
                     'KnW3vwmFwg8itOuGsDswqazAfcvbWqMhTafTLuZs04nNUBScc6sIqEzpUj++izHBaBTQCV9dx01QSY+SROwYHHfjcJHwS4rEP' \
                     'NlLj2cs4DBttqO/MKTpGozVm1xqFfUsyXY+hdAvO7zuvV+5KdIEbH11SfSeiVMlEHzK3N5jpaW9SdI4OzkWVlLTGDnnBUR+8t' \
                     'gOfruJE7nKnAijn6HhQ0RmpYaaPy8xMr5Tnw3AZ1/UwCluUdO47MzidmZ0Hq1GY42LXrIeOK3UVt/bRphZNdV7E0GjO55WPQ' \
                     'ucYc5R27Tacvtjm68QeaaVhfY6OqaAjC+MyY0pM2juWtRKYeNNFHLaXBHPBDR9wduhDis2cJxssKjUO2mMB0t1FXKLIXMC' \
                     'qfF5V7OR6ncI8C7Qdc+sULS5O01Vcu5Ypg8I/45jzFl3QBmxwWTJrQGFmdQcOMzSUjcF0bgSmhOmkTcnQfshGEZA8rHe' \
                     'XcYZCw3Ix6HNlOuO9ERLDwBirexG6jmLT/ioubBuwaTqvKia4kDuHtRlt0Gdlu1xo13G0gy37rJOZHCddEBFDB9XI7RSF' \
                     'ItgNuNdWzBFueOGwn1A5ejIwU96Kld7nKzhzOrIbzthiJkWM2LQXgr72eNK6S7gP6C5mfFBWGsFszkHlwIMpRAflqO/CVVVV' \
                     'Vf0PFPhxjC3RS44+Jd0pXm4umuOMlKerDf/1P1xRGJtG7jha/4XecLIo342Tc+CL2HDNLOUoN5wQsolg34sLjWIsjzsOdxby' \
                     'aaYooHtxqtlf3oMrFcKb8AUuNv52nN5wX0TnlkXejuMN2sAvX+BE4ymvN1fm0jM3xs843QgWF343TjXzuIQdR9pwvsEjMLm4m' \
                     '3GMx0xfjhKOk2zB8W1fae+O7qk3LWL/EO5tE6HqvyHx1OnvEFSH/HmePleF7Y01x1c357r9RqliQM/NiFfLLP4xnfclC6eW' \
                     'poxvppZRljUFuKwP3PNxvtcZsZnLO/84bphdmu3eNM8Vrc7ASXHgaNbT43wLFxux9O4TLohmzk0MbPeQXn7F7Zi/jrN+XDTi' \
                     'WDIthhH7kR0nG9qv8LEZ3e+j+z5uFhSYE6MC7rQRsvst6F0huU3Pfo+b5Vf3/qzAD4Wzmc1JZGx8VuYlnDjdVZxx5QHmubwdy6' \
                     'TgF81k+0OTfqnMoMZR2+PKEZ3jir9wWMm/gcMDH7hT7pykbpyb2T6vQITbrNCvWQ+zv4EjlNzaK5y36HEpgYWx' \
                     'L7hYruGX6e8xZO151n8HF5+VcpwjXL+UE26c2QczX678vUXsqJSPOHwwkVnIZdnM/PRLfxP3lXQxVxVrS' \
                     '0k6/skCfno8cdefmauqqqqqqqqqqqqqqqqq/t/6A5YxWhprcrw0AAAAAElFTkSuQmCC'

        movieurl = "https://openapi.naver." \
              "com/v1/search/movie.xml?yearfrom=2017&yearto=2019&query=" + movie_str  # xml 결과
        # "com/v1/search/movie.xml?start=1&yearfrom=1980&yearto=2019&query=" + query  # xml 결과
        request = urllib.request.Request(movieurl)
        request.add_header("X-Naver-Client-Id", client_id)
        request.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()

        if (rescode == 200):
            response_body = response.read()
        else:
            print("Error Code:" + rescode)
        data = response_body.decode('utf-8')

        tree = ElementTree.fromstring(data)

        image_url = []
        tmp=[]

        itemElements = tree.getiterator("item")  # return list type

        self.title = []  # 영화 제목
        self.openDt = []  # 개봉 년도
        self.pubDate = []  # 제작 년도
        self.director = []  # 영화 감독
        self.actor = []  # 출연 배우
        self.userRating = []  # 영화 평점
        self.searchimage = []  # 영화 제목


        tmp.clear()
        for item in itemElements:
            image = item.find("image")
            title = item.find("title")

            pubDate = item.find("pubDate")
            director = item.find("director")
            actor = item.find("actor")
            userRating = item.find("userRating")

            self.title.append(title.text)

            self.pubDate.append(pubDate.text)
            self.director.append(director.text)
            self.actor.append(actor.text)
            self.userRating.append(userRating.text)



            if image.text is not None:
                tmp.append(image.text)

        if len(tmp):
            self.searchimage.append(tmp[0])
        else:
            self.searchimage.append(noneimage2)


        self.text2.insert(INSERT, "영화 제목 : " + self.title[0].replace("<","").replace(">","").replace("b","").replace("/","") + "\n\n")
        self.text2.insert(INSERT, "개봉 년도 : " + self.pubDate[0] + "\n\n")
        self.text2.insert(INSERT, "영화 감독 : l" + self.director[0] + "\n\n")
        self.text2.insert(INSERT, "출연 배우 : l" + self.actor[0] + "\n\n")
        self.text2.insert(INSERT, "네티즌 평점 : " + self.userRating[0] + "\n\n")

        u = urlopen(self.searchimage[0])
        r_data = u.read()
        u.close()

        if Image.open(BytesIO(r_data)):
            im = Image.open(BytesIO(r_data))
        photo = ImageTk.PhotoImage(im)


        self.labelImage2 = Label(self.frame2, image=photo, background="gray11")
        self.labelImage2.image = photo
        self.labelImage2.place(x=323, y=230 )

    def Search_Button_Action(self):
        boxoffice_client_id = "475bf83ac2911d034998c841c40225c7"

        noneimage = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAG4AAACeCAMAAADkF8/QAAAAS1BMVEXp6el0dHTMzM' \
                    'yvr6+RkZHIyMi8vLz8/Pzm5ub////W1tbg4OCysrLd3d2srKygoKD09PSmpqaZmZnKysqDg4O/v7+Kiop7e3vw8PAN' \
                    'vY8LAAAF5UlEQVR4nO2ZCXOjOBCFhS5kHUji/v+/dF8LbMgkU7tZiPcovaqxCWT46NfdatlhrKqqqqqqqqqqqqqqqupfp' \
                    'ZTeSns83sdb28ejfaxvoqX20Qbbtu/hkZFWKfNo3wAjI5maOLfrG9JXjNTTwK0NP58+MlL5SSngrGl/1k4y0mihd1xYfzR' \
                    '9oLW26zRwQ8G59IPpIyN17Dxw4BUca3+Mlx6t62IngFPGkpvBGdj5I+VCRqq5z4TzASlEJwBn0o+kj+o/WZ17mOm9faD3gCP' \
                    'eT9iJtLUpoe65z5S89UHxFd796aP6xy3XFcAUJuE9x5mHIzsdyuXe9JGRDGEQmEI02msDXBtKubh7uw+xpQDbkCezhbii0xP' \
                    'xcMLB0Xu7L21l8QQiRItqQcgPQjJEmG61s20d2bYDSTjer60r0oeH2J7kFq1ta2nRImIRCC6E46f9/S7g+lgHZS0fFFReh+' \
                    '34o3j481v9JaUHli0hNJZKpSlQPpVwPwjrjL0UIFzchcbLfaeHYKzwqEfRd46ZkzZHubqIM6gO1MOagoydVtZxH+06yF4ObC' \
                    'tVQ5lkpTRX66/hUhmkKANm+xeOry7LGCgmqhCUpaM2hMJVHN/mNkzccRbRBWVRFg551N53nh84cT26rQf4EZ3Vo0osKPwEO4P' \
                    'KnW3vwmFwg8itOuGsDswqazAfcvbWqMhTafTLuZs04nNUBScc6sIqEzpUj++izHBaBTQCV9dx01QSY+SROwYHHfjcJHwS4rEP' \
                    'NlLj2cs4DBttqO/MKTpGozVm1xqFfUsyXY+hdAvO7zuvV+5KdIEbH11SfSeiVMlEHzK3N5jpaW9SdI4OzkWVlLTGDnnBUR+8t' \
                    'gOfruJE7nKnAijn6HhQ0RmpYaaPy8xMr5Tnw3AZ1/UwCluUdO47MzidmZ0Hq1GY42LXrIeOK3UVt/bRphZNdV7E0GjO55WPQ' \
                    'ucYc5R27Tacvtjm68QeaaVhfY6OqaAjC+MyY0pM2juWtRKYeNNFHLaXBHPBDR9wduhDis2cJxssKjUO2mMB0t1FXKLIXMC' \
                    'qfF5V7OR6ncI8C7Qdc+sULS5O01Vcu5Ypg8I/45jzFl3QBmxwWTJrQGFmdQcOMzSUjcF0bgSmhOmkTcnQfshGEZA8rHe' \
                    'XcYZCw3Ix6HNlOuO9ERLDwBirexG6jmLT/ioubBuwaTqvKia4kDuHtRlt0Gdlu1xo13G0gy37rJOZHCddEBFDB9XI7RSF' \
                    'ItgNuNdWzBFueOGwn1A5ejIwU96Kld7nKzhzOrIbzthiJkWM2LQXgr72eNK6S7gP6C5mfFBWGsFszkHlwIMpRAflqO/CVVVV' \
                    'Vf0PFPhxjC3RS44+Jd0pXm4umuOMlKerDf/1P1xRGJtG7jha/4XecLIo342Tc+CL2HDNLOUoN5wQsolg34sLjWIsjzsOdxby' \
                    'aaYooHtxqtlf3oMrFcKb8AUuNv52nN5wX0TnlkXejuMN2sAvX+BE4ymvN1fm0jM3xs843QgWF343TjXzuIQdR9pwvsEjMLm4m' \
                    '3GMx0xfjhKOk2zB8W1fae+O7qk3LWL/EO5tE6HqvyHx1OnvEFSH/HmePleF7Y01x1c357r9RqliQM/NiFfLLP4xnfclC6eW' \
                    'poxvppZRljUFuKwP3PNxvtcZsZnLO/84bphdmu3eNM8Vrc7ASXHgaNbT43wLFxux9O4TLohmzk0MbPeQXn7F7Zi/jrN+XDTi' \
                    'WDIthhH7kR0nG9qv8LEZ3e+j+z5uFhSYE6MC7rQRsvst6F0huU3Pfo+b5Vf3/qzAD4Wzmc1JZGx8VuYlnDjdVZxx5QHmubwdy6' \
                    'TgF81k+0OTfqnMoMZR2+PKEZ3jir9wWMm/gcMDH7hT7pykbpyb2T6vQITbrNCvWQ+zv4EjlNzaK5y36HEpgYWx' \
                    'L7hYruGX6e8xZO151n8HF5+VcpwjXL+UE26c2QczX678vUXsqJSPOHwwkVnIZdnM/PRLfxP3lXQxVxVrS' \
                    '0k6/skCfno8cdefmauqqqqqqqqqqqqqqqqq/t/6A5YxWhprcrw0AAAAAElFTkSuQmCC'


        self.now = datetime.now()


        movie_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList" \
                    ".xml?key=475bf83ac2911d034998c841c40225c7&targetDt=" + str(
            self.now.year * 10000 + self.now.month * 100 + self.now.day - 1)  # xml 결과

        req = urllib.request.Request(movie_url)

        data = urllib.request.urlopen(req).read()

        self.MmovieNm = []
        self.Mrank = []
        self.MshowRange = []
        self.MopenDt = []
        self.MaudiAcc = []
        self.MrankInten = []
        self.MsalesAcc = []

        self.Mimage = []

        tree = ElementTree.fromstring(data)

        itemElements = tree.getiterator("dailyBoxOffice")  # return list type
        # print(itemElements)

        for item in itemElements:
            movieNm = item.find("movieNm")
            rank = item.find("rank")
            openDt = item.find("openDt")
            audiAcc = item.find("audiAcc")  # 누적관객수
            rankInten = item.find("rankInten")  # 전날대비 순위변동
            salesAcc = item.find("salesAcc")  # 누적 매출

            self.MmovieNm.append(movieNm.text)
            self.Mrank.append(rank.text)
            self.MopenDt.append(openDt.text)
            self.MaudiAcc.append(audiAcc.text)
            self.MrankInten.append(rankInten.text)
            self.MsalesAcc.append(salesAcc.text)
            #self.maildata += "영화순위 : " + item.find("rank") + "위" + "영화제목 : " + item.find("movieNm") + "\n"

        ##################################################################################

        for i in range(10):
            tmp = []
            query = urllib.parse.quote(self.MmovieNm[i])
            # query = urllib.parse.quote("악인전")

            url = "https://openapi.naver." \
                  "com/v1/search/movie.xml?yearfrom=2017&yearto=2019&query=" + query  # xml 결과
                    #"com/v1/search/movie.xml?start=1&yearfrom=1980&yearto=2019&query=" + query  # xml 결과
            request = urllib.request.Request(url)
            request.add_header("X-Naver-Client-Id", client_id)
            request.add_header("X-Naver-Client-Secret", client_secret)
            response = urllib.request.urlopen(request)
            rescode = response.getcode()

            if (rescode == 200):
                response_body = response.read()
                # print(response_body.decode('utf-8'))
            else:
                print("Error Code:" + rescode)

            # data = urllib.request.urlopen(request).read()
            data = response_body.decode('utf-8')

            tree = ElementTree.fromstring(data)

            image_url = []

            itemElements = tree.getiterator("item")  # return list type

            # print("itemElement: ", itemElements)
            tmp.clear()
            for item in itemElements:
                # self.Mimage.append(noneimage)
                if item.find("image").text:
                    image = item.find("image")

                    print(image.text)

                    if image.text is not None:
                        tmp.append(image.text)

                    else:
                        tmp.append(noneimage)


                # print(tmp)
                # # print(tmp[0])

            if len(tmp):
                self.Mimage.append(tmp[0])
            else:
                self.Mimage.append(noneimage)



test()