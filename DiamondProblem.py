#Solving Diamond Problem In Python Using Super() Function.
class A:
    def __init__(self):
        print('Class A')
class B(A):
    def __init__(self):
        super().__init__()
        print('Class B')
class C(A):
    def __init__(self):
        super().__init__()
        print('Class C')
class D(C,B):
    def __init__(self):
        super().__init__()
        print('Class D')

if __name__ == '__main__':
    d = D()
