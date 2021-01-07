#We will explore all the design patterns that can be used in python to build a better and scaleable software.
#First we'll explore Decorator design pattern.

class ABC():
    def myfunction(self):
        print('ABC class function')
class DecoratorClass():
    def __init__(self,ABC):
        self.abc = ABC
    def myfunction(self):
        print('A simple Decorator')

def caller(abc):
    abc.myfunction()

a = ABC()
caller(DecoratorClass(a))


import time
def log_calls(func):
    print('Log Calls')
    def wrapper(*args, **kwargs):
        now = time.time()
        print("Calling {0} with {1} and {2}".format(
        func.__name__, args, kwargs))
        return_value = func(*args, **kwargs)
        print("Executed {0} in {1}ms".format(
        func.__name__, time.time() - now))
        return return_value
    return wrapper
@log_calls
def test1(a,b,c):
    print("\ttest1 called")
def test2(a,b):
    print("\ttest2 called")
def test3(a,b):
    print("\ttest3 called")
time.sleep(1)
test1 = log_calls(test1)
test2 = log_calls(test2)
test3 = log_calls(test3)
test1(1,2,3)
test2(4,b=5)
test3(6,7)



def decorater(func):
    def wrapper(*args):
        print(f'Decorater Function{args}')
        func(args)
    return wrapper
@decorater
def func2(x):
    print('Function that has to be decorated')

func2(10)



class ABC():
    def myfunction(self):
        print('ABC class function')
class DecoratorClass():
    def __init__(self,ABC):
        self.abc = ABC
    def myfunction(self):
        self.abc.myfunction()
        print('A simple Decorator')

def caller(abc):
    abc.myfunction()

a = ABC()
caller(DecoratorClass(a))


def mydecorator(function):
    def wrapped(*args, **kwargs):
        # do some stuff before the original
        # function gets called
        print(type(kwargs))
        result = function(*args, **kwargs)
        # do some stuff after function call and
        # return the result
        return result
    # return wrapper as a decorated function
    return wrapped
@mydecorator
def value(a,b):
    print(a+b)
value(10,2)

def MyClass():
    __private_value = 10
    def bro(self):
        self.__private_value = 11
print(dir(MyClass))


class Singleton():
    _instance = None
    def __new__(cls , *args,**kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls,*args,**kwargs)
        return cls._instance

a =  Singleton()
b = Singleton()
print(a==b)

'''Adpater Design Pattern'''

class TwoPin():
    def two_shoe(self):
        print('Two Shoe')
class ThreePlug():
    def three_shoe(self):
        print('Three Shoe')
class ThreePinAdpather(ThreePlug):
    def __init__(self,twopin):
        super().__init__()
        self.plug = twopin
    def three_shoe(self):
        self.plug.two_shoe()


a = TwoPin()
b =ThreePinAdpather(a)
b.three_shoe()

'''Using Meta Classes'''
from abc import ABCMeta , abstractclassmethod , abstractproperty , abstractmethod

class Duck(metaclass=ABCMeta):
    @abstractmethod
    def quack(self):
        ''''''
    @abstractmethod
    def fly(self):
        ''''''
class Dog():
    def Bark(self):
        print('Bark')
class DuckAdapter(Duck):
    def __init__(self):
        super().__init__()
        self.dog =  Dog()
    def quack(self):
        super().quack()
        self.dog.Bark()
    def fly(self):
        super().fly()

a = DuckAdapter()
a.quack()



from abc import ABC, abstractmethod


class Product(ABC):
    """
    The Product interface declares the operations that all concrete products
    must implement.
    """

    @abstractmethod
    def operation(self) -> str:
        pass


"""
Concrete Products provide various implementations of the Product interface.
"""


class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"



class Creator(ABC):
    """
    The Creator class declares the factory method that is supposed to return an
    object of a Product class. The Creator's subclasses usually provide the
    implementation of this method.
    """

    @abstractmethod
    def factory_method(self):
        """
        Note that the Creator may also provide some default implementation of
        the factory method.
        """
        pass

    def some_operation(self) -> str:
        """
        Also note that, despite its name, the Creator's primary responsibility
        is not creating products. Usually, it contains some core business logic
        that relies on Product objects, returned by the factory method.
        Subclasses can indirectly change that business logic by overriding the
        factory method and returning a different type of product from it.
        """

        # Call the factory method to create a Product object.
        product = self.factory_method()

        # Now, use the product.
        result = f"Creator: The same creator's code has just worked with {product.operation()}"

        return result


"""
Concrete Creators override the factory method in order to change the resulting
product's type.
"""


class ConcreteCreator1(Creator):
    """
    Note that the signature of the method still uses the abstract product type,
    even though the concrete product is actually returned from the method. This
    way the Creator can stay independent of concrete product classes.
    """

    def factory_method(self) -> ConcreteProduct1:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory_method(self) -> ConcreteProduct2:
        return ConcreteProduct2()



def client_code(creator: Creator) -> None:
    """
    The client code works with an instance of a concrete creator, albeit through
    its base interface. As long as the client keeps working with the creator via
    the base interface, you can pass it any creator's subclass.
    """

    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")

print("App: Launched with the ConcreteCreator1.")
client_code(ConcreteCreator1())
print("\n")
print("App: Launched with the ConcreteCreator2.")
client_code(ConcreteCreator2())
