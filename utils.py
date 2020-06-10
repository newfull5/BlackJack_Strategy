from matplotlib import pyplot as plt
import re
import random
import re
import random

class BlackJack():
    
    def __init__(self, always_insurance = False):
        num = ['A','2','3','4','5','6','7','8','9','10','J','Q','K'] #A to K
        pattern = ['C', 'H', 'S', 'D'] #Clover, Heart, Spade, Diamond

        self.deq = []

        for p in pattern:
            for n in num:
                self.deq.append(n+p)

        self.deq = self.deq * 4 #덱 4세트를 묶어서 진행, 총 208장
        
        random.shuffle(self.deq) # 셔플
        
        self.player_card = []
        self.player_point = []
        self.player_score = 0
        self.player_wins = 0
        self.splited = False
        
        self.dealer_card = []
        self.dealer_point = []
        self.dealer_score = 0
        
        self.insurance = always_insurance
        
        self.A = re.compile('A')
        self.T = re.compile('10|J|Q|K')
        
        
    def Begin(self):
        self.player_card.append(self.deq.pop()[:-1])
        self.player_card.append(self.deq.pop()[:-1])
        
        
    def Split(self,idx=0):
        if self.splited:
            temp = self.player_card[idx].pop()
            temp2 = self.player_card[idx].pop()
            del self.player_card[idx]
            self.player_card.append([temp])
            self.player_card.append([temp2])
        else:
            temp = self.player_card.pop()
            temp2 = self.player_card.pop()
            self.player_card.append([temp])
            self.player_card.append([temp2])
        self.splited = True
            
        
    def PointCalc(self,card):
        tmp = []
        self.player_point = []
        if self.splited:
            for c in card:
                self.player_point.append(self.CardSum(c))
        else:
            self.player_point.append(self.CardSum(card))
        
    def CardSum(self,card):
        temp = 0
        
        if card == '10':
            return 10
            
        elif self.A.search(''.join(card)):
            for c in card:
                if self.A.search(c):
                    temp += 11
                elif self.T.search(c):
                    temp += 10
                else:
                    temp += int(c)
                    
            if temp > 21:
                temp -= 10
            return temp
        
        elif self.T.search(''.join(card)):
            for c in card:
                if self.T.search(c):
                    temp += 10
                else:
                    temp += int(c)
            return temp
            
        else:
            return sum(map(int, card))
    
    
    def IsItBlackJack(self,card):
        if len(card) == 2:
            if self.A.search(''.join(card)) and self.T.search(''.join(card)):
                return True
        return False
    
        
    def HitOrStand(self, Hit=False, Stand=False, split=True, breakpoint=17):
        if Hit == True:
            if self.splited:
                for c in self.player_card:
                    if self.CardSum(c) > breakpoint:
                        continue
                        
                    c.append(self.deq.pop()[:-1])
                    if split and c[0] == c[1]:
                        self.Split(self.player_card.index(c))
                        continue
            else:
                if self.CardSum(self.player_card) <= breakpoint:
                    self.player_card.append(self.deq.pop()[:-1])
                
    def DealerFirstCard(self):
        self.dealer_card.append(self.deq.pop()[:-1])
#        if self.dealer_card[0] == 'A':
#            self.insurance = always_insurance
                
    def DealerCard(self):
        self.dealer_card.append(self.deq.pop()[:-1])
        if self.IsItBlackJack(self.dealer_card):
            if self.insurance:
                self.player_score -= 2
                
        while self.CardSum(self.dealer_card) < 17:
            self.dealer_card.append(self.deq.pop()[:-1])
            
        if self.CardSum(self.dealer_card) > 21:
            self.dealer_point = -1
        else:
            self.dealer_point = self.CardSum(self.dealer_card)

    def Burst(self):
        for c in self.player_point:
            if c > 21:
                self.player_point[self.player_point.index(c)] = -1
            
    def Compare(self):
        if self.splited:
            for p in self.player_point:
                if p == 21:
                    if p == 21:
                        continue
                    self.player_score += 2 # 블랙잭일 경우 2배를 받는 룰입니다
                    self.player_wins += 1
                    
                if p > self.dealer_point:
                    self.player_score += 2
                    self.player_wins += 1
                    
                elif p < self.dealer_point:
                    self.player_score -= 2
        else:
            if self.player_point[0] > self.dealer_point:
                self.player_score += 2
                self.player_wins += 1
                return 'P'
                
            elif self.player_point[0] < self.dealer_point:
                self.player_score -= 2
                return 'D'



breakpoint = 12
match_cnt = 0

dealer_first_card = {
    '11':0,
    '2':0,
    '3':0,
    '4':0,
    '5':0,
    '6':0,
    '7':0,
    '8':0,
    '9':0,
    '10':0
}

def DealerBurstCase():
    
    global match_cnt
    global dealer_first_card
        
    for _ in range(1000):



        a = BlackJack(always_insurance=False)

        while len(a.deq) > 10: #카드가 10장 미만일 경우 새게임

            a.player_card = []
            a.player_point = []
            a.splited = False
            a.dealer_card = []
            a.dealer_point = []

            a.Begin() #시작 플레이어 카드 두장 받기

            match_cnt += 1 #경기 횟수 +1

            a.PointCalc(a.player_card) #플레이어 카드 값 합계 계산

            if a.IsItBlackJack(a.player_card): # 블랙잭일 경우 다시
                continue

            a.DealerFirstCard() # 딜러 첫 카드 받기

            a.Burst() #플레이어 카드가 버스트 인지 체크

            a.DealerCard() #딜러 카드 받기

            if a.dealer_point == -1:
                dealer_first_card[str(a.CardSum(a.dealer_card[0]))] += 1



    print('딜러가 버스트 할 확률 : {:.2f}%'.format(100* sum(dealer_first_card.values())/match_cnt))
    lists = list(dealer_first_card.values())[:-1] + [list(dealer_first_card.values())[-1]//4]*4
    plt.bar(['A','2','3','4','5','6','7','8','9','10','J','Q','K'], lists)
    plt.show()

#12이하 스탠드


def WhenToHit(breakpoint):
    global dealer_first_card
    global match_cnt
    
    dealer_first_card = {
        '11':0,
        '2':0,
        '3':0,
        '4':0,
        '5':0,
        '6':0,
        '7':0,
        '8':0,
        '9':0,
        '10':0
    }

    breakpoint = breakpoint
    match_cnt = 0

    for _ in range(1000):

        a = BlackJack(always_insurance=False)

        while len(a.deq) > 10: #카드가 10장 미만일 경우 새게임

            a.player_card = []
            a.player_point = []
            a.splited = False
            a.dealer_card = []
            a.dealer_point = []

            a.Begin() #시작 플레이어 카드 두장 받기

            match_cnt += 1 #경기 횟수 +1

            a.PointCalc(a.player_card) #플레이어 카드 값 합계 계산

            if a.IsItBlackJack(a.player_card): # 블랙잭일 경우 다시
                continue

            a.DealerFirstCard() # 딜러 첫 카드 받기

            while min(a.player_point) < breakpoint:
                a.HitOrStand(Hit=True, breakpoint=breakpoint)
                a.PointCalc(a.player_card)

            a.Burst() #플레이어 카드가 버스트 인지 체크

            a.DealerCard() #딜러 카드 받기

            if a.Compare() == 'P':
                dealer_first_card[str(a.CardSum(a.dealer_card[0]))] += 1

    print('승률 : {:.2f}%'.format(100* sum(dealer_first_card.values())/match_cnt))
    lists = list(dealer_first_card.values())[:-1] + [list(dealer_first_card.values())[-1]//4]*4


