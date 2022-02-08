class A:
    def __init__(self, x):
        self.x = x

    # def __setattr__(self, key, value):
    #     print("__setattr__:", key, value)

    def __getattr__(self, item):
        print("__getattr__:", item)


a = A(10)
a.x
print(a.x)
# print(a.__dict__)
# print(a.__class__.__dict__)