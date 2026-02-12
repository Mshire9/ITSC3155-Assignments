import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    is_on = True

    while is_on:
        choice = input("What would you like? (small/medium/large/report/off): ").lower()

        if choice == "off":
            is_on = False

        elif choice == "report":
            print("Resources:")
            for item, amount in sandwich_maker_instance.resources.items():
                print(f"{item}: {amount}")
            print(f"Money: ${cashier_instance.profit}")

        elif choice in recipes:
            sandwich = recipes[choice]
            ingredients = sandwich["ingredients"]
            cost = sandwich["cost"]

            if sandwich_maker_instance.check_resources(ingredients):
                payment = cashier_instance.process_coins()
                if cashier_instance.transaction_result(payment, cost):
                    sandwich_maker_instance.make_sandwich(choice, ingredients)

        else:
            print("Invalid choice. Please choose small, medium, large, report, or off.")

if __name__=="__main__":
    main()
