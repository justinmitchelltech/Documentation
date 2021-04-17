import numpy as np

friend = 'Carly'
print(friend[1])

friends = ['Carly', 'Paulo', [1, 2, 3]]
print(friends[2])
for thing in friends:
    if type(thing) is str:
        print('String')
    elif type(thing) is list:
        print('List of length '+str(len(thing)))

for i in range(len(friends)):
    print(str(i)+': '+str(friends[i]))

for i in range(6+1):
    # print(i)
    continue

for i in np.arange(0, 6+.05, 0.1):
    # print(i)
    continue

print('\n')
a = [1, 2]
b = [4, 5]
c = a+b
print(c)
print(c[-1])
print(c[0:-1])  # <-- remember "up to but not including" !!
print(dir(c))  # print all of the available methods associated with it
print(4 in c)

bigString = 'This if for testing the split function'
splitted = bigString.split()
print(splitted)