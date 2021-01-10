# Reversed Iterator is used to reverse the sequence in reverse order.
list_ = [1,2,3,4,5,6]
for i in reversed(list_):
    print (i)
for i in list_.__reversed__():
    print (i)

# Enumerate Iterator is used when we have to get the index of each obj in list.
# What Enumerate Provide us with tuple with (index and value)
# The enumerate function returns a list of tuples, our for loop splits each tuple into
#two values, and the print statement formats them together. It adds one to the index
#for each line number, since enumerate , like all sequences is zero based

list_ = [3,12,41,2,412,415,3]

for index , value in enumerate(list_):
    print(f'Index:{index+1} Value:{value}')

# Zip is used to together to or more iteratble together, iteratable objects are those who have 
# __iter__ method in there class implementation or __next__ method.

zipped = list(zip(list_ , list_))
print(zipped)
# To unzip them just use zip(*zipped_object)
unzipped  = zip(*zipped)
print(list(unzipped))

#List comprehensions are used write loops in complex loops in simple readable one line manner.
# list comprehensions are not just fancy way of writing for loops but they are highly optimized too.
# The following code presents a comparison between a simple for loop and its list comprehension.

input_strings = ['1', '5', '28', '131', '3']
output_integers = []
for num in input_strings:
    output_integers.append(int(num))

output_integers = [int(num) for num in input_strings]
print(output_integers)
class Forward_list(list):
    def __iter__(self):
        super().__iter__()
        
list_ = Forward_list()
list_.__iter__()
def doexits(list_):
    a = list_.__iter__
    print(a)    

iterator=iter(output_integers)
output_integers = [num+next(iterator) for num in output_integers   ]
print(output_integers)