from Coffe_Machine_Proyect.coffee import CoffeeMenu

class CoffeMachine:
    def __init__(self, water, milk, coffe, money):
        self.water = water
        self.milk = milk
        self.coffe = coffe
        self.money = money
        self.machine_ingredients = [self.water, self.milk, self.coffe, self.money]

    def coffe_info(self) -> str:
        return f"Water : {self.water}\n Milk : {self.milk}\n Coffee : {self.coffe}\n Money : {self.money}\n"

    def choose_coffe_type(self):
        coffe_input = input("What would you like? (espresso/latte/cappuccino): ")
        match coffe_input:
            case "espresso":
                cof_bool = False
                for machin_ing, (ing_name, espresso_ing) in zip(self.machine_ingredients, CoffeeMenu.espresso.items()):
                    if machin_ing < espresso_ing:
                        print(f"Sorry there is not enough {ing_name}")
                        cof_bool = False
                        break
                    else:
                        cof_bool = True
                if cof_bool == True:
                    print("Here is your espresso. Enjoy!”")
            case "latte":
                print("latte option")
            case "espresso":
                print("cappuccino option")
            case "report":
                self.coffe_info()
            case "off":
                exit()
