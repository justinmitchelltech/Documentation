def aFunction(input):
    thing = input*10
    return thing

class aCar():
    def __init__(self, engine, doors, size):
        self.engine = engine
        self.doors = doors
        self.size = size
    def specs(self):
        print('Engine: ',str(self.engine),'\tDoors: ',str(self.doors),'\tSize: ',self.size)


#----------------------------------------------------
#   Script from here on

output = aFunction(4)
print(output)

carlysCar = aCar(4, 4, 'small')
justinsCar = aCar(6, 4, 'truck')

print(carlysCar.engine)
justinsCar.specs()