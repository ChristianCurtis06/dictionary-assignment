# Task 1: Restaurant Menu Update

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

# Add a new category called "Beverages" with at least two items
restaurant_menu ["Beverages"] = {"Coke": 2.50, "Lemonade": 2.99}

# Update the price of "Steak" to 17.99
restaurant_menu["Main Course"].update({"Steak": 17.99})

# Remove "Bruschetta" from "Starters"
restaurant_menu["Starters"].pop("Bruschetta")

for type, items in restaurant_menu.items():
    print(f"{type}:")
    for item, price in items.items():
        print(f"  {item}: ${price}")