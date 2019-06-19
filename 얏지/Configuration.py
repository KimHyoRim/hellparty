from dice import*

class Configuration:

    def __init__(self):
        self.configs = ["Category","Ones", "Twos","Threes","Fours","Fives","Sixes",
               "Upper Scores","Upper Bonus(35)","Three of a kind", "Four of a kind",
               "Full House(25)", "Small Straight(30)", "Large Straight(40)", "Yahtzee(50)",
               "Chance", "Lower Scores", "Total"]

    def getConfigs(self):
        return self.configs

    def score(self, row, d):

        s = 0
        if row >= 0 and row < 6:
            return self.scoreUpper(d, row + 1)
        if row == 8:
            s = self.scoreThreeOfKind(d)
        if row == 9:
            s = self.scoreFourOfKind(d)
        if row == 10:
            s = self.scoreFullHouse(d)
        if row == 11:
            s = self.scoreSmallStraight(d)
        if row == 12:
            s = self.scoreLargeStraight(d)
        if row == 13:
            s = self.scoreYahtzee(d)
        if row == 14:
            s = self.scoreChance(d)
        return s

        # 정적 메소드 : 객체생성 없이 사용 가능
        # row 에 따라 주사위 점수를 계산 반환 . 예를 들어 , row 가 0 이면 " Ones" 가 채점되어야 함을
        # 의미합니다 . row 가 2 이면 , " Threes" 가 득점되어야 함을 의미합니다 . row 가 득점 ( scored ) 하지
        # 않아야 하는 버튼 ( 즉 , UpperScore , UpperBonus , LowerScore , Total 등 ) 을 나타내는 경우
        # - 1 을 반환합니다 .

        # if (row >= 0 and row <= 6):
        #     return Configuration.scoreUpper(d, row + 1)
        # elif (row == 8):

    def scoreUpper(self, dice, num):

        count = 0
        for i in range(len(dice)):
            if dice[i].getRoll() == num:
                count += num
        return count
        pass
        # 정적 메소드 : 객체생성 없이 사용 가능
        # Upper Section 구성 ( Ones , Twos , Threes , ...) 에 대해 주사위 점수를 매 깁니다 . 예를 들어 ,
        # num 이 1 이면 " Ones" 구성의 주사위 점수를 반환합니다 . . . .

    def scoreThreeOfKind(self, dice):

        sum = 0
        for i in range(1, 6 + 1):
            cnt = 0
            for j in range(5):
                if i == dice[j].getRoll():
                    cnt += 1
                if cnt >= 3:
                    for a in range(5):
                        sum += dice[a].getRoll()
                    return sum
        return 0
        pass

    def scoreFourOfKind(self, dice):

        sum = 0
        for i in range(1, 6 + 1):
            cnt = 0
            for j in range(5):
                if i == dice[j].getRoll():
                    cnt += 1
                if cnt >= 4:
                    for a in range(5):
                        sum += dice[a].getRoll()
                    return sum

        return 0
        pass

    def scoreFullHouse(self, dice):

        tmp = []
        for i in range(5):
            tmp.append(dice[i].getRoll())
        if tmp.count(0) == 5:
            return 0
        tmp.sort()
        first = False
        second = False
        if tmp[0] == tmp[1]:
            first = True
            if tmp[2] == tmp[3] and tmp[3] == tmp[4]:
                second = True
        if tmp[0] == tmp[1] and tmp[1] == tmp[2]:
            first = True
            if tmp[3] == tmp[4]:
                second = True
        if first and second:
            return 25
        return 0
        pass

    def scoreSmallStraight(self, dice):

        #1 2 3 4  혹은 2 3 4 5 혹은 3 4 5 6 검사
        #1 2 2 3 4, 1 2 3 4 6, 1 3 4 5 6, 2 3 4 4 5 . . .

        tmp = []
        for i in range(5):
            tmp.append(dice[i].getRoll())
        tmp.sort()
        tmp2 = list(set(tmp))
        if len(tmp2) == 4:
            if tmp2[3] - tmp2[0] == 3:
                return 30
        if len(tmp2) > 4:
            if tmp2[3] - tmp2[0] == 3:
                return 30
            if tmp2[4] - tmp2[1] == 3:
                return 30

        return 0
        pass

    def scoreLargeStraight(self, dice):
        # 1 2 3 4 5 혹은 2 3 4 5 6 검사 . . .

        tmp = []
        for i in range(5):
            tmp.append(dice[i].getRoll())
        tmp.sort()
        tmp2 = list(set(tmp))
        # sum = 0
        if len(tmp2) > 4:
            if tmp2[4] - tmp2[0] == 4:
                return 40
        return 0
        pass


    def scoreYahtzee(self, dice):

        t = []
        for i in range(5):
            t.append(dice[i].getRoll())
        if t.count(0) == 5:
            return 0
        num = dice[0].getRoll()
        # check = True
        for i in range(0, 5):
            if num != dice[i].getRoll():
                return 0
            else:
                check = True
        if check:
            return 50
        pass

    def scoreChance(self, dice):
        sum = 0
        for i in range(len(dice)):
            sum += dice[i].getRoll()
        return sum
        pass

    def sumDice(self, d):

        pass