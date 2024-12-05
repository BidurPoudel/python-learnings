# eg of di

# class CoffeeMachine:
#     def __init__(self, coffee_beans):
#         self.coffee_beans = coffee_beans
    
#     def make_coffee(self):
#         print(f'Making coffee with {self.coffee_beans}')
    
# premium_coffee:str= 'Premium coffee beans'
# machine = CoffeeMachine(premium_coffee)
# machine.make_coffee()

# example without of di

# class CoffeeMachine:
#     def make_coffee(self):
#         print('Making coffee with coffee machine')

# class CoffeeShop:
#     def __init__(self):
#         self.coffee_maker = CoffeeMachine()  # coffee shop is tightly coupled with CoffeeMachine
        
        #If the shop wants to switch to using a FrenchPress, you’ll have to go into the shop’s code and change it. That’s bad because the shop is tightly tied to the coffee machine.
        
#     def serve_coffee(self):
#         self.coffee_maker.make_coffee()

# shop = CoffeeShop()
# shop.serve_coffee()


# example of dependency injection

class CoffeeMaker:
    def make_coffee(self):
        pass
    
class CoffeeShop:  #high module depends on abstraction (CoffeeMaker) not low modules
    def __init__(self, coffee_maker: CoffeeMaker):
        self.coffee_maker = coffee_maker

    def serve_coffee(self):
        self.coffee_maker.make_coffee()


# this are low modules which are implementing the abstraction
class CoffeeMachine(CoffeeMaker):
    def make_coffee(self):
        print('making coffee with coffee machine')

class FrenchPress(CoffeeMaker):
    def make_coffee(self):
        print('Making coffee with french press')


coffee_machine = CoffeeMachine()
french_press = FrenchPress()

shop1 = CoffeeShop(coffee_machine)
shop2 = CoffeeShop(french_press)

shop1.serve_coffee()
shop2.serve_coffee()