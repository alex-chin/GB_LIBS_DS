from random import shuffle

a = ['red'] * 23 + ['blue'] * 34
shuffle(a)
while len(a) >=2:
    # print(1,a)
    if a[0] == a[1]: # identical
        a.append('blue')  # put blue
    else:
        a.append('red')
    a.pop(0)
    a.pop(0)
    shuffle(a)
print(a)
