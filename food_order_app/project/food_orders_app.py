from typing import List

from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.meal import Meal
from project.meals.starter import Starter


class FoodOrdersApp:
    def __init__(self):
        self.menu: List[Meal] = []
        self.clients_list: List[Client] = []

    def check_menu_ready(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

    def find_client(self, phone_number):
        for client in self.clients_list:
            if client.phone_number == phone_number:
                return client

    def check_if_client_already_registered(self, phone_number):
        for client in self.clients_list:
            if client.phone_number == phone_number:
                return True

    def check_if_client_not_registered(self, phone_number):
        for client in self.clients_list:
            if client.phone_number != phone_number:
                return True

    def register_client(self, client_phone_number: str):
        if self.check_if_client_already_registered(client_phone_number):
            raise Exception("The client has already been registered!")
        client_number = Client(client_phone_number)
        self.clients_list.append(client_number)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        valid_types = ["Starter", "MainDish", "Dessert"]
        for meal in meals:
            if type(meal).__name__ in valid_types:
                self.menu.append(meal)

    def show_menu(self):
        self.check_menu_ready()
        details = [m.details() for m in self.menu]
        return "\n".join(details)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        self.check_menu_ready()
        if self.check_if_client_not_registered(client_phone_number):
            self.register_client(client_phone_number)
        client = self.find_client(client_phone_number)
        meals_to_order = []
        current_bill = 0
        for name, quantity in meal_names_and_quantities.items():
            for meal in self.menu:
                if meal.name == name:
                    if meal.quantity >= quantity:
                        meals_to_order.append(meal)
                        current_bill += meal.price + quantity
                        break
                    else:
                        raise Exception(F"Not enough quantity of {type(meal).__name__}: {name}!")
                else:
                    raise Exception(F"{name} is not on the menu!")

        client.shopping_cart.extend(meals_to_order)
        client.bill += current_bill

        return f"Client {client_phone_number} " \
               f"successfully ordered {', '.join(meal.name for meal in client.shopping_cart)} " \
               f"for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        pass

    def finish_order(self, client_phone_number: str):
        pass

    def __str__(self):
        pass


food_orders_app = FoodOrdersApp()
print(food_orders_app.register_client("0899999999"))
french_toast = Starter("French toast", 6.50, 5)
hummus_and_avocado_sandwich = Starter("Hummus and Avocado Sandwich", 7.90)
tortilla_with_beef_and_pork = MainDish("Tortilla with Beef and Pork", 12.50, 12)
risotto_with_wild_mushrooms = MainDish("Risotto with Wild Mushrooms", 15)
chocolate_cake_with_mascarpone = Dessert("Chocolate Cake with Mascarpone", 4.60, 17)
chocolate_and_violets = Dessert("Chocolate and Violets", 5.20)
print(food_orders_app.add_meals_to_menu(
    french_toast, hummus_and_avocado_sandwich,
    tortilla_with_beef_and_pork,
    risotto_with_wild_mushrooms,
    chocolate_cake_with_mascarpone,
    chocolate_and_violets))
print(food_orders_app.show_menu())
food = {"Hummus and Avocado Sandwich": 5,
        "Risotto with Wild Mushrooms": 1,
        "Chocolate and Violets": 4}
print(food_orders_app.add_meals_to_shopping_cart('0899999999', **food))
additional_food = {"Risotto with Wild Mushrooms": 2,
                   "Tortilla with Beef and Pork": 2}
print(food_orders_app.add_meals_to_shopping_cart('0899999999', **additional_food))




