class A:
    def __init__(self):
        print("A in int")
    def freature1():
        print("feature1 is working")
    def freature2():
        print("feature2 is working")
class B(A):
    def __init__(self):
        print("B in int")
        super().__init__()
    def freature3():
        print("feature3 is working")
    def freature4():
        print("feature4 is working")
a1 = B()

         