import csv
from distutils.command.build_scripts import first_line_re
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
    
    def create_image_info(self, new_list):
        new_data = self.get_data(new_list)
        return new_data
    
    
    def get_all_images(self):
        file_path = os.getcwd()
        for r,d,f in os.walk(file_path):
            for file in f:
                file_type = '.csv'
                if file.endswith(file_type):
                    file_path = os.path.join(r, file)
        
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(dict(row))
        
        
if __name__ == '__main__':
    # specify arguments through argpaser
    parser = argparse.ArgumentParser()
    parser.add_argument('--numbers', dest='num', type=int, nargs='+')
    parser.add_argument('--age', dest='age', type=str)
    parser.add_argument('--name', dest='name', type=str)
    parser.add_argument('--num', dest='new_list', type=int, nargs='+')
    
    
    args = parser.parse_args()
    
    person = Person(args.age, args.name)
    print(person.create_image_info(args.new_list))
    # print('Before adding the list')
    # print(person.__dict__)
    # print('dir', person.__setattr__('age', 29))
    
    
    # print(person.get_data(args.num))
    # print('After adding the list')
    
    # print(person.get_all_images())
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