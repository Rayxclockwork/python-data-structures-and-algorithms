class Diner:
    def __init__(self, print_func=print, input_func=input):
        self.print = print_func
        self.input = input_func

    def dine(self):
        self.print('Welcome to TDD Diner')
        self.print('Home of the hottest cup of joe')
        main_dish = self.input('Enter a Main Dish: ')
        side_dish = self.input('Enter a Side Dish: ')

        self.print(f'One order of {main_dish} with {side_dish} coming up')


if __name__ == "__main__":

    def angry_print(msg):
        print('How dare you?' + msg)
    diner = Diner(angry_print)
    diner.dine()
