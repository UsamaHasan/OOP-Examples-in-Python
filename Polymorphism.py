"""The concept of Polymorphism is basically driven from chemistry where a element has a similar chemical
equation but different shape/orientation, such different shapes are known as polymorphs. In OOP 
Two classes drived from  a same base class can have different implementation of a same method/Function.
The Process of methods/function having different implementation but same name is called overriding.
Consider AudioFile as Baseclass to all the formats of such file and its child e.g MP3FILE and WAVFILE etc"""
class AudioFile():
    def __init__(self):
        pass
class MP3File(AudioFile):
    def play(self):
        pass
class OGGFile(AudioFile):
    def play(self):
        pass
class WAVFile(AudioFile):
    def play(self):
        pass

#Meta Programing in Python and the concept of Abstract Base Class aka abc's and the decorator 
#@abstractmethod.
#In the same way that a class functions as a template for the creation of objects, 
# a metaclass functions as a template for the creation of classes.
# Metaclasses are sometimes referred to as class factories

class Meta(type):
    def __new__(cls,name,bases,dict):
        x = super().__new__(cls,name,bases,dict)
        x.attr = 100
        return x
class Foo(metaclass=Meta):
    pass
print(Foo.attr)

print(Foo.__dict__)
from abc import abstractmethod , ABCMeta

class ABC(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        print("Abstract Class")
    def all(self):
        print("I work for all classes")
class Child(ABC):
    def foo(self):
        print('Child Class')
class Me():
    pass

child = Child()
print(child.all())

assert isinstance(Child(),ABC)
assert issubclass(Child,ABC)

ABC.register(Me)

assert issubclass(Me,ABC)


##
#@Property Decorator And Function Discription.
#
class Person():
    #
    def __init__(self,name,last_name):
        super().__init__()
        self.name = name
        self.last_name = last_name
        self._email = f'{self.name}{self.last_name}@mydomain.com'
    #A
    @property
    def email(self):
        return self._email 
    #
    @email.setter
    def email(self,e):
        self._email = e
    #
    #     
    @email.deleter
    def email(self):
        self._email = 'None'
    def __repr__(self):
        return f"Person Object:{self.name}{self.last_name}"

p = Person('Usama','Hasan')
a=repr(p)
print(a)
p.email = 'usamahasan72@gmail.com'
p.last_name ='Rao'
print(p.email)
del p.email
print(p.email)
