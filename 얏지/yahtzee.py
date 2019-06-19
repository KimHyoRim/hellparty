from tkinter import*
from tkinter import font
import tkinter.messagebox
from realPlayer import*
#from dice import*
from Configuration import*



class YahtzeeBoard:
    UPPERTOTAL = 6  # UpperScore 범주 인덱스
    UPPERBONUS = 7  # UpperBonus 범주 인덱스
    LOWERTOTAL = 15  # LowerScore 범주 인덱스


    dice = [] # Dice 객체 리스트
    diceButtons = []  # diceButton 리스트
    fields = [] # 각 플레이어 점수판 2 차원 리스트
                # 열 플레이어 , 0 열 = 플레이어 1, 1 열 = 플레이어 2,…
                #17 행 점수 = 카테고리 13 행 + upperScore + upperBonus + LowerScore + Total
    finish = []
    totalScore = []

    def __init__(self):
        self.InitPlayers()
        self.bottomLabel = None
        self.players = []   # player 객체 리스트
        self.numPlayers = 0
        self.player = 0     # 플레이어 순서를 제어
        self.round = 0  # 13라운드를 제어
        self.roll = 0   # 각 라운드 마다 3번 굴리기 roll을 할 수 있음

        self.TOTAL = 16

    def InitPlayers(self):
        self.pwindow = Tk()
        self.TempFont = font.Font(size = 16, weight = 'bold', family = 'Consolas')
        self.label = []
        self.entry = []
        self.label.append(Label(self.pwindow, text = "플레이어 명수", font = self.TempFont))
        self.label[0].grid(row = 0, column = 0)

        for i in range(1, 11):
            self.label.append(Label(self.pwindow, text = "플레이어"+str(i)+" 이름", font = self.TempFont))
            self.label[i].grid(row = i, column = 0)

        for i in range(11):
            self.entry.append(Entry(self.pwindow, font = self.TempFont))
            self.entry[i].grid(row = i, column = 1)
        self.playerPicButton = tkinter.Button(self.pwindow, text = "Yahtzee 플레이어 설정 완료", font= self.TempFont, command = self.playerNames).grid(row = 11, column = 0)
        self.pwindow.mainloop()

    def playerNames(self):
        self.numPlayers = int(self.entry[0].get())
        self.players = []
        for i in range(1, self.numPlayers + 1):
            self.players.append(Player(str(self.entry[i].get())))
        self.pwindow.destroy()

        self.player = 0
        self.round = 0
        self.roll = 0
        self.TOTAL = 16
        self.bonus = 0

        self.initInterface()

    def initInterface(self): # yahtzee 보드 윈도우 생성
        self.window = Tk("Yahtzee Game")
        self.window.geometry("1600x800")
        self.TempFont = font.Font(size = 16, weight = "bold", family = "Consolas")

        self.finish = [False for i in range(self.numPlayers)]
        self.totalScore = [0 for i in range(self.numPlayers)]

        for i in range(5):
            self.dice.append(Dice())
        self.scoreConfi = Configuration()

        self.rollDice = Button(self.window, text = "Roll Dice", font = self.TempFont, command = self.rollDiceListener) # Roll Dice 버튼
        self.rollDice.grid(row = 0, column = 0)

        for i in range(5): # dice 버튼 5개 생성
            self.diceButtons.append(Button(self.window, text = "?", font = self.TempFont, width = 8, command = lambda row = i:
                                           self.diceListener(row)))
            # 각각의 dice 버튼에 대한 이벤트 처리 diceListener 연결
            # 람다 함수를 이용하여 diceListener 매개변수 설정하면 하나의 Listener로 해결
            self.diceButtons[i].grid(row = i + 1, column = 0)

        for i in range(self.TOTAL + 2): # i행 : 점수
            Label(self.window, text = self.scoreConfi.configs[i], font = self.TempFont).grid(row = i, column = 1)
            for j in range(self.numPlayers): # j열 : 플레이어
                if i == 0:
                    Label(self.window, text = self.players[j].toString(), font = self.TempFont).grid(row = i, column = 5 + j)
                else:
                    if j == 0: # 각 행마다 한 번씩 리스트 추가, 다중 플레이어 지원
                        self.fields.append(list())
                    # i - 1행에 플레이어 개수 만큼 버튼 추가하고 이벤트 Listener 설정, 매개변서 설정
                    self.fields[i-1].append(Button(self.window, text = "", font = self.TempFont, width = 8, command = lambda row = i -1:
                                                   self.categoryListener(row)))
                    self.fields[i-1][j].grid(row = i, column = 5 +j)
                    # 누를 필요없는 버튼은 disable 시킴
                    if (j != self.player or (i - 1) == self.UPPERTOTAL or (i-1) == self.UPPERBONUS or (i-1) == self.LOWERTOTAL or (i - 1) == self.TOTAL):
                        self.fields[i-1][j]["state"] = "disabled"
                        self.fields[i-1][j]["bg"] = "light gray"

    # 상태 메세지 출력
        self.bottomLabel = Label(self.window, text = self.players[self.player].toString()+ "차례: Roll Dice 버튼을 누르세요", width = 35, font = self.TempFont)
        self.bottomLabel.grid(row = self.TOTAL + 2, column = 0)
        self.window.mainloop()

    def rollDiceListener(self):
        for i in range(5):
            if(self.diceButtons[i]["state"] != "disabled"):
                self.dice[i].rollDice()
                self.diceButtons[i].configure(text = str(self.dice[i].getRoll()))

        if self.roll == 0 or self.roll ==1:
            self.roll += 1
            self.rollDice.configure(text ="Roll Again")
            self.bottomLabel.configure(text = "보관할 주사위 선택 후 Roll Again")
        elif self.roll == 2:
            self.bottomLabel.configure(text = "카테고리를 선택하세요")
            self.rollDice["state"] = "disabled"
            self.rollDice["bg"] = "light gray"

        for i in range(6):
            if not self.players[self.player].getUsed(i):
                tmp = self.scoreConfi.score(i, self.dice)
                self.fields[i][self.player].configure(text=str(tmp))
        for i in range(6, 13):
            if not self.players[self.player].getUsed(i):
                tmp = self.scoreConfi.score(i + 2, self.dice)
                self.fields[i + 2][self.player].configure(text=str(tmp))

    def diceListener(self, row):
        self.diceButtons[row]["state"] = "disabled"
        self.diceButtons[row]["bg"] = "light gray"

    def categoryListener(self, row):

        self.score = self.scoreConfi.score(row, self.dice) # 점수계산
        index = row
        if row > 7:
            index = row - 2

        # 선택한 카테고리 점수 적고 disable 시킴
        self.players[self.player].setScore(self.score, index)
        # self.players[self.player].setAtUsed(index)
        self.fields[row][self.player].configure(text = str(self.score))
        self.fields[row][self.player]["state"] = "disabled"
        self.fields[row][self.player]["bg"] = "light gray"

        # UPPER category가 전부 사용되었으면 Upper Score, UpperBonus 계산
        if self.players[self.player].allUpperUsed():
            self.fields[self.UPPERTOTAL][self.player].configure(text = str(self.players[self.player].getUpperScore()))
            if self.players[self.player].getUpperScore() > 63:
                self.bonus = 35
                self.fields[self.UPPERBONUS][self.player].configure(text = "35") # UPPERBONUS = 7
            else:
                self.fields[self.UPPERBONUS][self.player].configure(text = "0") # UPPERBONUS = 7

        # # LOWER category 전부 사용되었으면 LOWER SCORE 계산
        # if (self.players[self.player].allLowerUsed()):
        #
        # # UPPER category 와 LOWER category 가 전부 사용되었으면 TOTAL 계산
        # if (self.players[self.player].allUpperUsed() and self.players[self.player].allLowerUsed()):

        if self.players[self.player].allLowerUsed():
            self.fields[15][self.player].configure(text=str(self.players[self.player].getLowerScore()))
            pass

        if self.players[self.player].allUpperUsed() and self.players[self.player].allLowerUsed():
            self.totalScore[self.player] = self.players[self.player].getUpperScore() + self.players[self.player].getLowerScore() + self.bonus
            self.fields[16][self.player].configure(text=str(self.totalScore[self.player]))
            pass

        # # 다음 플레이어로 넘어가고 선택할 수 없는 카테고리들은 disable 시킴
        # self.player = (self.player + 1) % self.numPlayers
        # for i in range(self.TOTAL + 1):
        #     for j in range(self.numPlayers):

        if self.numPlayers > 1:
            for i in range(17):
                self.fields[i][self.player]['state'] = 'disabled'
                self.fields[i][self.player]['bg'] = "light gray"
            for i in range(6):
                if not self.players[self.player].getUsed(i):
                    self.fields[i][self.player]["text"] = ""
            for i in range(7):
                if not self.players[self.player].getUsed(i + 6):
                    self.fields[i + 8][self.player]["text"] = ""

        if self.player == 0:
            self.round += 1
        if self.round >= 13:
            self.finish[self.player] = True

        print(self.finish.count(True))
        if self.finish.count(True) == self.numPlayers:
            m = 0
            ii = 0
            for i in range(self.numPlayers):
                if self.totalScore[i] > m:
                    m = self.totalScore[i]
                    ii = i
            Label(self.window,
                  text=self.players[ii].toString() + "이(가) " + str(self.totalScore[ii]) + "점으로 이겼습니다.",
                  font=self.TempFont, background="light gray").place(x=100, y=350)

        self.player = (self.player + 1) % self.numPlayers

        for i in range(6):
            if self.fields[i][self.player]["text"] is "":
                self.fields[i][self.player]['state'] = 'normal'
                self.fields[i][self.player]['bg'] = "light gray"
            elif self.numPlayers > 1:
                self.fields[i][self.player]['bg'] = "light gray"
        for i in range(8, 15):
            if self.fields[i][self.player]["text"] is "":
                self.fields[i][self.player]['state'] = 'normal'
                self.fields[i][self.player]['bg'] = "light gray"


        for i in range(self.TOTAL + 1):
            for j in range(self.numPlayers):
                pass

        self.roll = 0
        self.bottomLabel.configure(text='다시 굴리세요')
        self.rollDice['state'] = 'normal'
        self.rollDice['bg'] = "light gray"
        for i in range(5):
            self.diceButtons[i]['state'] = 'normal'
            self.diceButtons[i].configure(text='?')
            self.diceButtons[i]['bg'] = "light gray"

    # def categoryListener(self, row):
    #
    #     pass
    #
    #
    #
    # def categoryListener(self, row):
    #
    #     pass
    #     # # 라운드 증가 시키고 종료 검사
    #     # if (self.player == 0):
    #     #     self.round += 1
    #     # if (self.round == 13):
    #     #
    #     # # 다시 Roll Dice와 diceButtons 버튼 활성화, bottomLabel 초기화



YahtzeeBoard()
