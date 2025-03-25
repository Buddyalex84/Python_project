menu = {
        "Main Course": {"Paneer Butter Masala": 250, "Veg Biryani": 200, "Dal Makhani": 180},
        "Cold Coffee": {"Classic Cold Coffee": 120, "Mocha": 150, "Hazelnut Coffee": 170},
        "Sandwich": {"Cheese Sandwich": 100, "Veg Club Sandwich": 150, "Grilled Paneer Sandwich": 180},
        "Pizza": {"Margherita": 250, "Farmhouse": 300, "Peppy Paneer": 350}
}

order_total = 0
order=[]

print("Welcome to our Cafe\nHere is our menu:")
lst=['Main Course\nCold Coffee\nSandwich\nPizza']

if lst =='Main Course':
    print({"Paneer Butter Masala": 250, "Veg Biryani": 200, "Dal Makhani": 180})
elif lst =='Cold Coffe':
    print({"Classic Cold Coffee": 120, "Mocha": 150, "Hazelnut Coffee": 170})
elif lst == 'Sandwich':
    print({"Cheese Sandwich": 100, "Veg Club Sandwich": 150, "Grilled Paneer Sandwich": 180})
elif lst =='Pizza':
    print({"Margherita": 250, "Farmhouse": 300, "Peppy Paneer": 350})



item1=input("Enter your order...\n")
if item1  in lst:
    order_total += menu[item1]
    print(f"your order {item1} added in your list ")
else:
    print(f"Your order{item1} is not available yet")

