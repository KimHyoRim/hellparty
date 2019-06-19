class Player:
    UPPER = 6 # upper category 6개
    LOWER = 7 # lower category 7개
    def __init__(self, name):
        self.name = name
        self.score = [0 for i in range(self.UPPER + self.LOWER)] # 13개 category 점수
        #13개 category 사용 여부
        self.used = [False for i in range(self.UPPER + self.LOWER)]

    def setScore(self, score, index):
        self.score[index] = score
        self.used[index] = True
        pass

    def setAtUsed(self, index):

        pass

    def getUpperScore(self):
        s = 0
        for i in range(6):
            s += self.score[i]
        return s
        pass

    def getLowerScore(self):
        s = 0
        for i in range(self.UPPER, self.UPPER + self.LOWER):
            s += self.score[i]
        return s
        pass

    def getUsed(self, index):
        return self.used[index]
        pass

    def getTotalScore(self):
        pass

    def toString(self):
        return self.name

    def allLowerUsed(self):
        for i in range(self.UPPER, self.UPPER + self.LOWER):
            if self.used[i] == False:
                return False
        return True
        pass

    def allUpperUsed(self): # lower category 7개 모두 사용되었는가?
                            # upper category 6개 모두 사용되었는가?
                            # UpperScores, UpperBonus 계산에 활용
        for i in range(self.UPPER):
            if(self.used[i] == False):
               return False
        return True

