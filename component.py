class Button():
    p = 2
    def __init__(self) :
        self.data = 2

bt = Button()
b2 = Button()
bt.p = 3
b2.p = 4
print(bt.p)
print(b2.p)