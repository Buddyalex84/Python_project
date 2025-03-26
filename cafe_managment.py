def cafe_management():
    menu = {
        "Main Course": {"Paneer Butter Masala": 250, "Veg Biryani": 200, "Dal Makhani": 180},
        "Cold Coffee": {"Classic Cold Coffee": 120, "Mocha": 150, "Hazelnut Coffee": 170},
        "Sandwich": {"Cheese Sandwich": 100, "Veg Club Sandwich": 150, "Grilled Paneer Sandwich": 180},
        "Pizza": {"Margherita": 250, "Farmhouse": 300, "Peppy Paneer": 350}
    }
    
    total_bill = 0
    order = []
    
    print("\nWelcome to the Cafe! \nHere is our menu:")
    for category, items in menu.items():   #show category
        print(f"\n{category}:")
        for item, price in items.items():
            print(f"  {item} - Rs. {price}")
    
    while True:
        print("\nChoose a category:")     
        for i, category in enumerate(menu.keys(), 1):  
            print(f"{i}. {category}")
        print("5. Exit & Generate Bill")    #user click 5 to exit and generate bill.
        
        try:
            choice = int(input("Enter your choice (1-5): "))
            if choice == 5:
                break
            
            category_name = list(menu.keys())[choice - 1]
            print(f"\nYou chose {category_name}. Select an item:")
            
            items_list = list(menu[category_name].items())
            for j, (item, price) in enumerate(items_list, 1):
                print(f"{j}. {item} - Rs. {price}")
            
            item_choice = int(input("Enter your choice (1-3): "))
            selected_item, item_price = items_list[item_choice - 1]
            
            total_bill += item_price
            order.append((selected_item, item_price))
            print(f"{selected_item} added to your order!")
        
        except (ValueError, IndexError):
            print("Invalid choice! Please try again.")
    
    print("\nYour Order Summary:")
    for item, price in order:
        print(f"{item} - Rs. {price}")
    print(f"Total Bill: Rs. {total_bill}")
    print("Thank you for visiting our cafe! Have a great day!")
    
if __name__ == "__main__":
    cafe_management()
