from flask import Flask, request, jsonify

app = Flask(__name__)


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
        self.items.append(food.name)
        self.total += food.price


class Delivery:
    def __init__(self, status):
        self.status = status



customer = None
order = Order()
history = []

menu = [
    Food("Paneer", "Veg", 200, True),
    Food("Chicken", "Non-Veg", 300, True),
    Food("Juice", "Beverage", 100, True),
    Food("IceCream", "Dessert", 150, False)
]



@app.route("/")
def home():
    return "Food Delivery App Running 🚀"



@app.route("/create", methods=["POST"])
def create_account():
    global customer
    data = request.json

    customer = Customer(data["id"], data["name"], data["password"])
    return jsonify({"message": "Account Created!"})



@app.route("/login", methods=["POST"])
def login():
    global customer
    data = request.json

    if customer is None:
        return jsonify({"error": "Create account first!"})

    if customer.id != data["id"] or customer.password != data["password"]:
        return jsonify({"error": "Invalid Login!"})

    return jsonify({"message": "Login Successful!"})



@app.route("/menu", methods=["GET"])
def get_menu():
    menu_list = []
    for f in menu:
        menu_list.append({
            "name": f.name,
            "category": f.category,
            "price": f.price,
            "available": f.available
        })
    return jsonify(menu_list)



@app.route("/add", methods=["POST"])
def add_food():
    global order
    data = request.json
    item_name = data["item"]

    for f in menu:
        if f.name == item_name:
            if not f.available:
                return jsonify({"error": "Item not available!"})

            order.add_food(f)
            history.append(f"Added: {f.name}")
            return jsonify({"message": "Added!", "total": order.total})

    return jsonify({"error": "Item not found"})



@app.route("/finish", methods=["GET"])
def finish_order():
    global order

    response = {
        "total": order.total,
        "items": order.items
    }

    if order.total > 5000:
        response["approval"] = "Manager/Chef Approval Required"
    else:
        response["approval"] = "Order Approved"

    delivery = Delivery("Dispatched")
    response["delivery_status"] = delivery.status

    response["history"] = history

    return jsonify(response)



app.run(host="0.0.0.0", port=5001)
