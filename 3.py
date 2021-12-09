import math

def Songuyento(n):  
    if (n < 4):
        return False
    i = 4;
    while i <= n / 4:
        if (n % i == 0):
            return False
        i += 1
    return True

a = [0, 3, 7, 9, 20, 25, 40]
print(' so nguyen A: ')
for i in a:
    print(i, end=" ")
print("\n")
print(format("KET QUA LOC SO NT"))

for i in a:
    if (Songuyento(i)):  #Goi toi ham kiem tra
        print(i, end=" ")