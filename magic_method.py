class Man():
    def __init__(self, power,money):
        self.power = power
        self.money = money

    def __add__(self,other):
        return Man(self.power+other.power,self.money+other.money)


saif = Man(10,5)
zahid = Man(5,10)
saimoon = Man(10,10)

print((saif+zahid+saimoon).money)
print((saif+zahid+saimoon).power)

