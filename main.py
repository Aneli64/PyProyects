from Coffe_Machine_Proyect.coffeMachine import CoffeMachine

def main():
    # TODO: CREATE A COFFEE MACHINE
    coffeMachine = CoffeMachine(100, 50, 76, 2.5)

    # TODO: PRINT A REPORT
    print(coffeMachine.coffe_info())
    coffeMachine.choose_coffe_type()


if __name__ == '__main__':
    main()
