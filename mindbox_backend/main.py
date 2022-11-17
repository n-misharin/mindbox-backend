class A:
    def __init__(self):
        print(2)

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        print(1)
        return instance


a = A()
b = A()
c = A()
