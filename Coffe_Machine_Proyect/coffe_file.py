class Coffe:
    water = 0
    milk = 0
    coffe = 0
    money = 0.0

    def coffe_info(self) -> str:
        return f"Water : {self.water}\n Milk : {self.milk}\n Coffee : {self.coffe}\n Money : {self.money}\n"

    def coffe_type(self):
        coffe_input = input("What would you like? (espresso/latte/cappuccino): ")

        match coffe_input:
            case "espresso":
                print("espresso option")
            case "latte":
                print("latte option")
            case "espresso":
                print("cappuccino option")
            case "report":
                self.coffe_info()
            case "off":
                exit()

coffee1 = Coffe()
print(coffee1.coffe_info())