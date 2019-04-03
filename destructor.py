class Phone:
    # constructor
    def __init__(self,name,model,price):
        self.name = name
        self.model = model
        self.price = price

    def show_price(self):
        return self.price

nokia2330 = Phone('Nokia','2330',5000)


print(nokia2330.show_price())

del nokia2330

print(nokia2330.show_price())