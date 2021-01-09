#Tuples are Immutable and are used to bundle different types of object together.
#Tuples are used to store data; behavior cannot be stored in a tuple.
Student = 'Usama' , 12 , 12 , 12
print(type(Student))

#Named Tuples are used when you have to name objects that we are bundling together.
#The namedtuple constructor accepts two arguments. The first is an identifier for the
#named tuple. The second is a string of space-separated attributes that the named
#tuple can have. The first attribute should be listed, followed by a space, then the
#second attribute, then another space, and so on.
from collections import namedtuple

Stock = namedtuple("Stock","high current low")
stock = Stock(12,13,14)
print(stock.high)
print(stock.current)
print(stock.low)

#Dictionaries

stock = {"GOOG":(1,2,3),
    "MEZINO" : (2,3,4)}

try:
    print(stock['MEZINO'])
except KeyError:
    print('Wrong Key Entered')
finally:
    print('Thank You!')
# If the key Doesnot exist it  will return None, or the String entered at the second argument.
print(stock.get("Facebook",'None'))

#if the key is present it will return the value if it isn't then it will set the value provided at the
#second argument.
stock.setdefault('Nissan',(12,412,134))
print(stock['Nissan'])

#Keys() function will return all the keys in the dictionary over an iterator.
for keys in stock.keys():
    print(keys)
#Values() function will return will return all the values stored against key in dictionary.
for values in stock.values():
    print(values)
#Items() function will return tuples of keys and their corresponding values.
for keys , values in stock.items():
    print(f'Key:{keys},Value:{values}')

# We can update value anytime in dict.
stock['GOOG'] = (231,1244,124)

random_keys = {}
random_keys['2'] = 2
random_keys[2] =3
random_keys[(12,2)] = 4

from collections import defaultdict
def letter_frequency(sentence):
    frequencies = defaultdict(int)
    for letter in sentence:
        frequencies[letter] += 1
    return frequencies
a  = letter_frequency('This is me bitch ahmad')

num_items = 0
def tuple_counter():
    global num_items
    num_items += 1
    return (num_items, [])
d = defaultdict(tuple_counter)
d['a'][1].append("Hello")
d['b'][1].append("World")
d['a'][1].append("Bye")
print(d)
for keys , values in d.items():
    print(f'Key:{keys}, Values:{values}')
import string
CHARACTER =  list(string.ascii_letters) + [""]
print(CHARACTER)

from abc import abstractmethod


class BaseClass():
    @abstractmethod    
    def abc(self):
        print("Virtual Class.")
class ChildClass(BaseClass):
    def abc(self):
        print("Child Class")

base = ChildClass()
base.abc()
print(type(base))

print(ChildClass.__class__)
print(type(ChildClass()))
print(isinstance(base,BaseClass))