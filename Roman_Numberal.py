import random

global num
num = random.randrange(1,3001)
value = num
li = []
while True:
    if (num - 1000) >= 0:
        num -= 1000
        li.append("M")
    elif (num >= 500) and (num < 1000):
        if (num - 900) >= 0:
            num -= 900
            li.append("CM")
        elif (num - 800) >= 0:
            num -= 800
            li.append("DCCC")
        elif (num - 700) >= 0:
            num -= 700
            li.append("DCC")
        elif (num - 600) >= 0:
            num -= 600
            li.append("DC")
        elif (num - 500) >= 0:
            num -= 500
            li.append("D")
    elif (num < 500) and (num >= 100):
        if (num - 400) >= 0:
            num -= 400
            li.append("CD")
        elif (num - 300) >= 0:
            num -= 300
            li.append("CCC")
        elif (num - 200) >= 0:
            num -= 200
            li.append("CC")
        elif (num - 100) >= 0:
            num -= 100
            li.append("C")
    elif (num < 100) and (num >= 50):
        if (num - 90) >= 0:
            num -= 90
            li.append("XC")
        elif (num - 80) >= 0:
            num -= 80
            li.append("LXXX")
        elif (num - 70) >= 0:
            num -= 70
            li.append("LXX")
        elif (num - 60) >= 0:
            num -= 60
            li.append("LX")
        elif (num - 50) >= 0:
            num -= 50
            li.append("L")
    elif (num < 50) and (num >= 10):
        if (num - 40) >= 0:
            num -= 40
            li.append("XL")
        elif (num - 30) >= 0:
            num -= 30
            li.append("XXX")
        elif (num - 20) >= 0:
            num -= 20
            li.append("XX")
        elif (num - 10) >= 0:
            num -= 10
            li.append("X")
    elif (num < 10) and (num >= 5):
        if (num - 9) >= 0:
            num -= 9
            li.append("IX")
        elif (num - 8) >= 0:
            num -= 8
            li.append("VIII")
        elif (num - 7) >= 0:
            num -= 7
            li.append("VII")
        elif (num - 6) >= 0:
            num -= 6
            li.append("VI")
        elif (num - 5) >= 0:
            num -= 5
            li.append("V")
    elif (num < 5) and (num >= 1):
        if (num - 4) >= 0:
            num -= 4
            li.append("IV")
        elif (num - 3) >= 0:
            num -= 3
            li.append("III")
        elif (num - 2) >= 0:
            num -= 2
            li.append("II")
        elif (num - 1) >= 0:
            num -= 1
            li.append("I")




    else:
        break

string = "".join(li)
print(value)
print(string)
