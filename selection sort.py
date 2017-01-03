import random 
SIZE = 10
list = [i for i in range(SIZE)]
random.shuffle(list)
print ("Initial list")
print (list)

def luna(n):
    for i in range(SIZE):
        min = 100
        minind = i
        for j in range(i,SIZE):
            if n[j] < min:
                min = n[j]
                minind = j
        n[minind] = n[i]
        n[i] = min
        print (n)

a = luna(list)
print (a)
