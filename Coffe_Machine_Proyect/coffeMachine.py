from Coffe_Machine_Proyect.coffee import CoffeeMenu


class CoffeMachine:
    def __init__(self, water, milk, coffe, money):
        self.water = water
        self.milk = milk
        self.coffe = coffe
        self.money = money
        self.machine_ingredients = [self.water, self.milk, self.coffe]

    def coffe_info(self) -> str:
        return f"Water : {self.water}\n Milk : {self.milk}\n Coffee : {self.coffe}\n"

    def available_coffe(self, coffee_type: str) -> bool:
        bool_coffee = False
        match coffee_type:
            case "espresso":
                coffee = CoffeeMenu.espresso
            case "latte":
                coffee = CoffeeMenu.latte
            case "cappuccino":
                coffee = CoffeeMenu.cappuccino
            case "off":
                bool_coffee = False
                exit()
            case _:
                bool_coffee = False
                print("Invalid coffee type")
                return False

        for machine_ing, (ing_name, coffee_ing) in zip(self.machine_ingredients, coffee.items()):
            if machine_ing < coffee_ing:
                print(f"Sorry, there is not enough {ing_name}")
                return False
            else:
                return True

    def choose_coffe_type(self):
        coffe_input = input("What would you like? (espresso/latte/cappuccino): ")
        coins_in_machine = 0.0
        cost_of_coffee = 0.0

        if self.available_coffe(coffe_input):
            coins_input = float(input("Insert coins: "))
            match coffe_input:
                case "espresso":
                    cost_of_coffee = CoffeeMenu.espresso["cost"]
                case "latte":
                    cost_of_coffee = CoffeeMenu.latte["cost"]
                case "cappuccino":
                    cost_of_coffee = CoffeeMenu.cappuccino["cost"]
                case _:
                    exit()
            while coins_in_machine < cost_of_coffee:
                coins_in_machine += coins_input
                print(f"COINS IN MACHINE: {coins_in_machine}")
                if coins_in_machine >= cost_of_coffee:
                    change = coins_in_machine - cost_of_coffee
                    break
                coins_input = float(input("Insert coins: "))

            print(f"Enjoy your coffee!!, your change is: {change}")
