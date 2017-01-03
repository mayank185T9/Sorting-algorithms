import random
SIZE = 10
list = [i for i in range(SIZE)]
random.shuffle(list)
print ("Original:", list)

def luna(n):
    for i in range(SIZE):
        y = i
        for j in range(i):
            if i == 0:
                break
            if n[y] > n[y-1]:
                break
            else:
                temp = n[y-1]
                n[y-1] = n[y]
                n[y] = temp
            y = y - 1
        print (n)

a = luna(list)
print (a)
