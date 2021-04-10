# Read the file line by line and count the lines
print('Round 1 -------------------------------------------------------------------')
fh = open('Data/abcs_practice.txt')
count = 0
for line in fh:
    print(line)
    # print(line.rstrip())  # Strips '\n''s and whitespace off of right side of ln
    count = count + 1
print('\nLine Count: '+str(count))
fh.close()

# Read the file as one thing and give it back in 1 string
print('\nRound 2 -------------------------------------------------------------------')
filename = input('Enter filename of file in Data folder:\t')
try:
    fh = open('Data/'+filename+'.txt')
except:
    print('That filename cannot be opened. Shutting down program...')
    quit()  # Necessary so the rest doesn't run
string = fh.read()
print(string)
