import random
import math

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
        eqt = '(' + str(a * b * c) + '÷' + str(a * b) + ')' + '-' + '(' + str(e) + '-' + str(d) + ')'
        ans = (c) - (e - d)
    elif case == 14 :
        eqt = str(a) + '×' + str(b) + '×' + str(c)
        ans = a * b * c
    elif case == 15 :
        eqt = str(a) + '+' + str(b) + '+' + str(c)
        ans = a + b + c
    
    return eqt , str(ans)

def get_exercise_pro(level) :

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

    case = random.randint(1 , 15)

    if case == 1:
        eqt = get_tf(a) + ' ∧ ' + get_tf(b)
        ans = a and b
    elif case == 2:
        eqt = get_tf(a) + ' ∨ ' + get_tf(b)
        ans = a or b
    elif case == 3:
        eqt = '~' + get_tf(a) + ' ∨ ' + get_tf(b)
        ans = (not a) or b
    elif case == 4:
        eqt = get_tf(b) + ' ∧ '+ '~' + get_tf(a)
        ans = (not a) and b
    elif case == 5:
        eqt = '~' + get_tf(b) + ' ∧ '+ '~' + get_tf(a)
        ans = not(a or b)
    elif case == 6:
        eqt = '~' + get_tf(b) + ' ∨ '+ '~' + get_tf(a)
        ans = not(a and b)
    elif case == 7:
        eqt = get_tf(a) + ' ∧ ' + get_tf(b) +  ' ∧ ' +'~' + get_tf(c)
        ans = a and b and (not c)
    elif case == 8:
        eqt = '~' + '(' + get_tf(a) + ' ∧ ' + get_tf(b) + ')' + ' ∨ '+ '~' + get_tf(c)
        ans = not(a and b) or (not c)
    elif case == 9:
        eqt = '~' + '(' + get_tf(a) + ' ∨ ' + get_tf(b) + ')' + ' ∧ '+ get_tf(c)
        ans = not(a or b) and c
    elif case == 10:
        eqt = '(' + get_tf(a) + ' ∨ ' + get_tf(b) + ')' + ' ∧ '+ '(' + get_tf(c) + ' ∨ ' + get_tf(d) + ')'
        ans = (a or b) and (c or d)

    return eqt , get_tf(ans)

for i in range(1 , 15):
    eqt , ans = get_exercise_real(i)
    print(ans + " " + eqt)
for i in range(1 , 10):
    eqt , ans = get_exercise_pro(i)
    print(ans + " " + eqt)