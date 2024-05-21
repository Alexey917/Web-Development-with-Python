a = int(input("продажи 1 менеджера "))
b = int(input("продажи 2 менеджера: "))
c = int(input("продажи 3 менеджера: "))
zp1=0
zp2=0
zp3=0
oklad = 200
if a>1000:
    zp1 = oklad+a*0.08
elif a <500:
    zp1 = oklad+a*0.03
elif a >500 and a<1000:
    zp1 = oklad+a*0.05

if b>1000:
    zp2 = oklad+b*0.08
elif b <500:
    zp2 = oklad+b*0.03
elif a >500 and a<1000:
 zp2 = oklad+b*0.05
if c>1000:
    zp3 = oklad+c*0.08
elif c <500:
    zp3 = oklad+c*0.03
elif a >500 and a<1000:
    zp3 = oklad+c*0.05

if zp1 > zp2 and zp1 > zp3:
    zp1 += 200
    print("лучший -1 менеджер " + str(zp1))

if zp2 > zp1 and zp2 > zp3:
    zp1 += 200
    print("лучший -2 менеджер " + str(zp2))
if zp3 > zp1 and zp3 > zp2:
    zp1 += 200
    print("лучший -3 менеджер " + str(zp3))