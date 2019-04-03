def show(func):
    def design(num):
        return 'Number {}'.format(func(num))

    return design


@show

def getNum(num):
    return num**2

print(getNum(16))