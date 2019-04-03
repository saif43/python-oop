class Player:
    university = 'UIU' # Class Variable
    # constructor
    def __init__(self, name, score):

        # instance Variable
        self.name = name
        self.score = score

    def makeScore(self, score):
        self.score += score
        print(self.name,' made score',score)

zahid = Player("Zahid",0)
reza  = Player("Reza",0)

print(zahid.university)
print(reza.university)

print('----------------------')


print(zahid.name,zahid.score)
print(reza.name,reza.score)

zahid.makeScore(1)

print(zahid.name,zahid.score)
print(reza.name,reza.score)