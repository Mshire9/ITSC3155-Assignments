class SandwichMaker:
    def __init__(self, resources):
        self.resources = resources

    def check_resources(self, ingredients):
        """Return True if there are enough resources, else False."""
        for item in ingredients:
            if ingredients[item] > self.resources.get(item, 0):
                print(f"Sorry there is not enough {item}.")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct required ingredients from resources."""
        for item in order_ingredients:
            self.resources[item] -= order_ingredients[item]
        print(f"Here is your {sandwich_size} sandwich. Enjoy!")