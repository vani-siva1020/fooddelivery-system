
class Customer:
    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self.password = password



class Food:
    def __init__(self, name, category, price, available):
        self.name = name
        self.category = category
        self.price = price
        self.available = available



class Order:
    def __init__(self):
        self.items = []
        self.total = 0

    def add_food(self, food):
        self.items.append(food)
        self.total += food.price



class Delivery:
    def __init__(self, status):
        self.status = status



def main():
    customer = None

    # 🔹 Available Food List
    menu = [
        Food("Paneer", "Veg", 200, True),
        Food("Chicken", "Non-Veg", 300, True),
        Food("Juice", "Beverage", 100, True),
        Food("IceCream", "Dessert", 150, False)
    ]

    history = []

    while True:
        print("\n--- MAIN MENU ---")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        main_choice = int(input("Enter choice: "))

       
        if main_choice == 1:
            id = int(input("Enter ID: "))
            name = input("Enter Name: ")
            password = input("Set Password: ")

            customer = Customer(id, name, password)
            print("Account Created!")

       
        elif main_choice == 2:
            if customer is None:
                print("Create account first!")
                continue

            login_id = int(input("Enter ID: "))
            login_pass = input("Enter Password: ")

            if customer.id != login_id or customer.password != login_pass:
                print("Invalid Login!")
                continue

            print("Login Successful!")

          
            order = Order()

            while True:
                print("\n--- MENU ---")
                for i, f in enumerate(menu):
                    status = "" if f.available else " [Not Available]"
                    print(f"{i+1}. {f.name} ({f.category}) - {f.price}{status}")

                print("5. Finish Order")

                choice = int(input("Choose item: "))

                if 1 <= choice <= 4:
                    selected = menu[choice - 1]

                    if not selected.available:
                        print("Item not available!")
                    else:
                        order.add_food(selected)
                        history.append(f"Added: {selected.name}")
                        print("Added!")

                elif choice == 5:
                    break

          
            print("Total Amount:", order.total)

           
            if order.total > 5000:
                print("Approval Required:")
                print("1. Manager Approval")
                print("2. Chef Approval")
            else:
                print("Order Approved!")

           
            delivery = Delivery("Dispatched")
            print("Delivery Status:", delivery.status)

           
            print("\nTransaction History:")
            for h in history:
                print(h)

        elif main_choice == 3:
            print("Exit...")
            break

        else:
            print("Invalid Choice")



main()
