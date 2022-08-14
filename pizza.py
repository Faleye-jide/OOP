from tqdm import tqdm

class Pizza:
    '''Create a Pizza class '''
    
    def __init__(self, toppings: int, size: str, tax: int, extra_cheese: bool) -> None:
        '''constructor defintion for initialization of attributes'''
        self.toppings = toppings
        self.size = size
        self.tax = tax
        self.extra_cheese = extra_cheese
        
    def get_price(self):
        total_price: float = 0.0
        if self.size == 'large':
            total_price += 10.0
        else:
            total_price += 8.0
        
        total_price += self.toppings * 0.75
        
        if self.extra_cheese:
            total_price += 1.0
            
        if self.tax:
            total_price += 1.50 
        
        return f'The total price of the pizza is ${total_price}'    
    
    
    
    
pizza: Pizza = Pizza(1.5, 'large', 1.50, False)
another_pizza: Pizza = Pizza(2, 'small', 1.50, True)
# pizza.self.size = 'large'
# pizza.self.extra_cheese = False
# pizza.self.tax = 2.50
# pizza.self.toppings = 3

print(Pizza)
print(pizza.get_price())
print(another_pizza.get_price())
        