class A():
    def work(self):
        print('Work A')


class B(A):
    def work(self):
        print('Work B')
        super().work()

B().work()