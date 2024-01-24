class A:
    def __init__(self):
        print("A in int")
    def freature1():
        print("feature1 is working")
    def freature2():
        print("feature2 is working")
class B():
    def __init__(self):
        print("B in int")
    def freature3():
        print("feature3 is working")
    def freature4():
        print("feature4 is working")
class C(A,B):
    def __init__(self):
        print("C in int")
        super().__init__()
a1=C()