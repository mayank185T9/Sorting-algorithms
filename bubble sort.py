import random
SIZE = 10
list = [i for i in range(SIZE)]
random.shuffle(list)
print ("Original:", list)

def luna(n):
    while True:
        x = 0
        for i in range(SIZE-1):
            if n[i] > n[i+1]:
                temp = n[i+1]
                n[i+1] = n[i]
                n[i] = temp
                x += 1
        if x == 0:
            print (n)
            break

a = luna(list)
print (a)



    
