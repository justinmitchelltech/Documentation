string1 = 'test'

range1 = range(0, len(string1))
range2 = range(len(string1))
print('\nrange(0, len(string1)) == range(len(string1))\n', range2 == range1, '\n')

for i in range1:
    print(string1[i])

for letter in string1:
    print(letter, '\t', ord(letter))