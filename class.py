import os
import shutil
from datetime import datetime

class Person:

    def __init__(self, age, name , data_list=[]) -> None:
        self.age = age
        self.name = name
        self.data_list =  data_list
    
    def get_data(self, nums):
        for num in nums:
            self.data_list.append()
        return self.data_list
    


# `setattr(person, 'age', 10) 
# print(getattr(person, 'age'))
# if hasattr(person, 'age'):
#     print('Yes')
# else:
#     print('No')
    
    
# attribute = person.__dict__
# for key, value in attribute.items():
#     print(f'{key}: {value}')`