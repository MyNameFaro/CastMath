import random
import math
import numpy as np



COUSE1 = 120
COUSE2 = 50
COUSE3 = 20
COUSE4 = 20

class Data():
    def __init__(self , data = [0 , 0] , c = 0 , level = 1):
        self.X = []
        self.Y = []
        self.model = []
        self.c = c #Critical
        self.level = level #LEVEL
        self.CRITICAL = 4
        self.m = 0
        self.e = 0
        for d in data:
            self.X.append([1 , len(self.X) + 1])
            self.Y.append([d])
    def train(self) :
        X = np.matrix(self.X)
        Y = np.matrix(self.Y)
        a = X.getT().dot(X)
        b = a.getI().dot(X.getT())
        #print(a)
        self.model = b.dot(Y)

        #set m and m previous
        self.m = self.model[1 , 0]
        self.e = self.model[0 , 0]
    def test(self, y):
        if y < self.e + (self.m * (len(self.X) + 1)) : #LINEAR 
            self.c -= 1 
        elif y > self.e + (self.m * (len(self.X) + 1)) : #LINEAR 
            self.c += 1 
    def append(self , data) :
        for d in data:
            #self.data.append([len(self.data) + 1 , d])
            self.X.append([1 , len(self.X) + 1])
            self.Y.append([d])
    def get_m(self) :
        return self.m
    def get_data(self) :
        data = []
        for y in self.Y :
            data.append(y[0])
        return data
    def get_level(self):
        return self.level
    def update(self):
        if self.c >= self.CRITICAL :
            self.level += 1
            self.c = 0
        elif self.c <= (-1 * self.CRITICAL) :
            self.level -= 1
            self.c = 0



def get_exercise_real(level=1) :
    def get_num(level) :
        return random.randint(math.pow(10 , level - 1) , math.pow(10 , level) - 1)

    eqt = ""
    ans = 0

    a = get_num(level)
    b = get_num(level)
    c = get_num(level)
    d = get_num(level)
    e = get_num(level)

    case = random.randint(1 , 15)

    if case == 1 :
        eqt = str(a) + '+' + str(b)
        ans = a + b
    elif case == 2 :
        if a < b :
            a += b
        eqt =  str(a) + '-' + str(b)
        ans = a - b
    elif case == 3 :
        eqt = str(a * b) + '÷' + str(b)
        ans = a 
    elif case == 4 :
        eqt = str(a) + '×' + str(b)
        ans = a * b
    elif case == 5 :
        if a < b :
            a += b
        eqt = str(c) + '+' + '(' + str(a) + '-' + str(b) + ')'
        ans = c + a - b
    elif case == 6 :
        if a < c :
            a += c
        eqt = '(' + str(a * b) + '÷' + str(b) + ')' + '-' + str(c)
        ans = (a) - c
    elif case == 7 :
        eqt = str(c) + '+' +  '(' + str(a) + '×' + str(b) + ')'
        ans = c + (a * b)
    elif case == 8 :
        eqt = '(' + str(a) + '×' + str(b) + ')' + '+' + '(' + str(c) + '×' + str(d) + ')'
        ans = (a * b) + (c * d)
    elif case == 9 :
        if (a * b) < (c * d) :
            a += c
            b += d
        eqt = '(' + str(a) + '×' + str(b) + ')' + '-' + '(' + str(c) + '×' + str(d) + ')'
        ans = (a * b) - (c * d)
    elif case == 10 :
        if c < d :
            c += d
        eqt = '(' + str(a) + '+' + str(b) + ')' + '×' + '(' + str(c) + '-' + str(d) + ')'
        ans = (a + b) * (c - d)
    elif case == 11 :
        if c < d :
            c += d
        eqt = '(' + str(a) + '×' + str(b) + ')' + '×' + '(' + str(c) + '-' + str(d) + ')'
        ans = (a * b) * (c - d)
    elif case == 12 :
        if c < d :
            c += d
        eqt = '(' + str(a * b) + '÷' + str(b) + ')' + '×' + '(' + str(c) + '-' + str(d) + ')'
        ans = (a) * (c - d)
    elif case == 13 :
        if e < d :
            e += d
        if c < (e - d):
            c += (e - d)
        eqt = '(' + str(a * b * c) + '÷' + str(a * b) + ')' + '-' + '(' + str(e) + '-' + str(d) + ')'
        ans = (c) - (e - d)
    elif case == 14 :
        eqt = str(a) + '×' + str(b) + '×' + str(c)
        ans = a * b * c
    elif case == 15 :
        eqt = str(a) + '+' + str(b) + '+' + str(c)
        ans = a + b + c
    
    return eqt , str(ans)

def get_exercise_pro(level=1) :

    value = [True , False]

    def get_tf(pro):
        if pro : 
            return 'T'
        else : 
            return 'F'

       
    eqt = ""
    ans = 0
    
    a = random.choice(value)
    b = random.choice(value)
    c = random.choice(value)
    d = random.choice(value)

    case = random.randint(1 , 10)

    if case == 1:
        eqt = get_tf(a) + ' ^ ' + get_tf(b)
        ans = a and b
    elif case == 2:
        eqt = get_tf(a) + ' V ' + get_tf(b)
        ans = a or b
    elif case == 3:
        eqt = '~' + get_tf(a) + ' V ' + get_tf(b)
        ans = (not a) or b
    elif case == 4:
        eqt = get_tf(b) + ' ^ '+ '~' + get_tf(a)
        ans = (not a) and b
    elif case == 5:
        eqt = '~' + get_tf(b) + ' ^ '+ '~' + get_tf(a)
        ans = not(a or b)
    elif case == 6:
        eqt = '~' + get_tf(b) + ' V '+ '~' + get_tf(a)
        ans = not(a and b)
    elif case == 7:
        eqt = get_tf(a) + ' ^ ' + get_tf(b) +  ' ^ ' +'~' + get_tf(c)
        ans = a and b and (not c)
    elif case == 8:
        eqt = '~' + '(' + get_tf(a) + ' ^ ' + get_tf(b) + ')' + ' V '+ '~' + get_tf(c)
        ans = not(a and b) or (not c)
    elif case == 9:
        eqt = '~' + '(' + get_tf(a) + ' V ' + get_tf(b) + ')' + ' ^ '+ get_tf(c)
        ans = not(a or b) and c
    elif case == 10:
        eqt = '(' + get_tf(a) + ' V ' + get_tf(b) + ')' + ' ^ '+ '(' + get_tf(c) + ' V ' + get_tf(d) + ')'
        ans = (a or b) and (c or d)

    return eqt , get_tf(ans)


#x = Data([2 , 4])
#x.train()
#print(x.get_m())
#x.append([6 ,8 ,10])
#x.train()
#p#rint(x.get_m())
#print(x.X)
#print(x.Y)
#y = x.get_data()
#print(y)