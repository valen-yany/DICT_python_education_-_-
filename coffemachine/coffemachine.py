class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.disposable_cups = 9
        self.money = 550
        self.status = 'action'
        self.statuses = ('action', 'making coffee', 'filling water', 'filling milk', 'filling beans',
                         'filling cups', 'taking money', 'checking of remains', 'off')
        self.coffees = (1, 2, 3)

    def action(self, action: str):
        actions = ("buy", "fill", "take", "remaining", "exit")
        if action not in actions:
            return None
        if action == actions[0]:
            self.status = self.statuses[1]
        elif action == actions[1]:
            self.status = self.statuses[2]
        elif action == actions[2]:
            self.status = self.statuses[6]
        elif action == actions[3]:
            self.status = self.statuses[7]
        elif action == actions[4]:
            self.status = self.statuses[8]

    def coffee(self, coffee: str):
        coffee_action = ('1', '2', '3', "back")
        if coffee not in coffee_action:
            return None
        if coffee == coffee_action[3]:
            self.status = self.statuses[0]
            return None
        if self.disposable_cups < 1:
            print("Sorry, not enough disposable cups!")
            self.status = self.statuses[0]
            return None
        if coffee == coffee_action[0]:
            if self.water < 250:
                print("Sorry, not enough water!")
                self.status = self.statuses[0]
                return None
            elif self.coffee_beans < 16:
                print("Sorry, not enough coffee beans!")
                self.status = self.statuses[0]
                return None
            self.water -= 250
            self.coffee_beans -= 16
            self.money += 4
        elif coffee == coffee_action[1]:
            if self.water < 350:
                print("Sorry, not enough water!")
                self.status = self.statuses[0]
                return None
            elif self.milk < 75:
                print("Sorry, not enough milk!")
                self.status = self.statuses[0]
                return None
            elif self.coffee_beans < 20:
                print("Sorry, not enough coffee beans!")
                self.status = self.statuses[0]
                return None
            self.water -= 350
            self.milk -= 75
            self.coffee_beans -= 20
            self.money += 7
        elif coffee == coffee_action[2]:
            if self.water < 200:
                print("Sorry, not enough water!")
                self.status = self.statuses[0]
                return None
            elif self.milk < 100:
                print("Sorry, not enough milk!")
                self.status = self.statuses[0]
                return None
            elif self.coffee_beans < 12:
                print("Sorry, not enough coffee beans!")
                self.status = self.statuses[0]
                return None
            self.water -= 200
            self.milk -= 100
            self.coffee_beans -= 12
            self.money += 6
        self.disposable_cups -= 1
        print("I have enough resources, making you a coffee!")
        self.status = self.statuses[0]

    def fill_water(self, milliliters: int):
        self.water += milliliters
        self.status = self.statuses[3]

    def fill_milk(self, milliliters: int):
        self.milk += milliliters
        self.status = self.statuses[4]

    def fill_beans(self, grams: int):
        self.coffee_beans += grams
        self.status = self.statuses[5]

    def fill_cup(self, cups: int):
        self.disposable_cups += cups
        self.status = self.statuses[0]

    def take_money(self):
        print(f"I gave you {self.money}")
        self.money = 0
        self.status = self.statuses[0]

    def check_remainings(self):
        print(f"""\nThe coffee machine has:
{self.water} of water
{self.milk} of milk
{self.coffee_beans} of coffee beans
{self.disposable_cups} of disposable cups
{self.money} of money""")
        self.status = self.statuses[0]

    def enter(self):
        while self.status != self.statuses[8]:
            if self.status == self.statuses[0]:
                print("\nWrite action(buy,fill,take,remaining,exit):")
                input_line = input()
                self.action(input_line)
                continue
            elif self.status == self.statuses[1]:
                print("""What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to 
main menu:""")
                input_line = input()
                self.coffee(input_line)
                continue
            elif self.status == self.statuses[2]:
                print("Write how many ml of water you want to add:")
                input_line = input()
                self.fill_water(int(input_line))
                continue
            elif self.status == self.statuses[3]:
                print("Write how many ml of milk you want to add:")
                input_line = input()
                self.fill_milk(int(input_line))
                continue
            elif self.status == self.statuses[4]:
                print("Write how many grams of coffee beans you want to add:")
                input_line = input()
                self.fill_beans(int(input_line))
                continue
            elif self.status == self.statuses[5]:
                print("Write how many disposable cups you want to add:")
                input_line = input()
                self.fill_cup(int(input_line))
                continue
            elif self.status == self.statuses[6]:
                self.take_money()
                continue
            elif self.status == self.statuses[7]:
                self.check_remainings()
                continue


coffee_machine = CoffeeMachine()
coffee_machine.enter()
