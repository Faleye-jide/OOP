import os
import shutil
import argparse
from datetime import datetime

class Person:

    def __init__(self, age, name , data_list=[]) -> None:
        self.age = age
        self.name = name
        self.data_list =  data_list
    
    def get_data(self, nums):
        for num in nums:
            if num % 2 != 0:
                self.data_list.append(num)
        return self.data_list
    

if __name__ == '__main__':
    # argpaser
    parser = argparse.ArgumentParser()
    parser.add_argument('--numbers', dest='num', type=int, nargs='+')
    parser.add_argument('--age', dest='age', type=str)
    parser.add_argument('--name', dest='name', type=str)
    
    
    args = parser.parse_args()
    
    person = Person(args.age, args.name)
    print('Before adding the list')
    print(person.__dict__)
    
    print(person.get_data(args.num))
    print('After adding the list')
    
    print(person.__dict__) # To get all the attributes of an object


# person: Person = Person('jide',28)
# # person.name = 'jide'
# # person.age = 28
# nums = [1,2,3,4,5,6]
# print(person.get_data(nums))

# `setattr(person, 'age', 10) 
# print(getattr(person, 'age'))
# if hasattr(person, 'age'):
#     print('Yes')
# else:
#     print('No')
    
    
# attribute = person.__dict__
# for key, value in attribute.items():
#     print(f'{key}: {value}')`