import numpy as np


class doStuff:
    def __init__(self, var1=0, var2=0, var3=0):
        self.var1 = var1
        self.Exvar2 = var2
        self.var3 = var3
    x = np.array([1])
    def addStuff(self, a):
        self.x = np.append(self.x, a)


# New class that inherits doStuff, then extends it by adding var4 to existing stuff
class doMoreStuff(doStuff):
    var4 = 'newestStuff'


# test = doStuff()
test = doStuff(1, 2, 3)
test.addStuff(7)
test.addStuff(9)
print(test.x)
print(type(test))
print(dir(test))

# test2 = doMoreStuff(5, 6, 7)
test2 = doMoreStuff()
print(test2.x)