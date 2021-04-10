string1 = 'test'

range1 = range(0, len(string1))
range2 = range(len(string1))
print('\nrange(0, len(string1)) == range(len(string1))\n', range2 == range1, '\n')

for i in range1:
    print(string1[i])

for letter in string1:
    print(letter, '\t', ord(letter))

print('\n', string1.upper())

print('\n', type(string1))

str2 = 'Testing this out.'
print(str2.replace('Testing', '123'))

str3 = 'Testing out if you can find justin@wahoofitness.com from this string.'
atpos = str3.find('@')
nxtspace = str3.find(' ', atpos)
print(str3[atpos+1:nxtspace])

print('\n', '© Justin Mitchell 🤘 Spring 2021')