import os
from datetime import datetime
from PIL import Image
import qrcode

def cafe_management():
    def admin_portal():
        while True:
            print("\n🔐 Admin Portal:")
            print("1. View All Bills")
            print("2. View Total Sales Today")
            print("3. Continue to Cafe System")
            print("4. Exit")

            choice = input("Enter choice (1-4): ")
            if choice == "1":
                if os.path.exists("bill_history.txt"):
                    print("\n📂 All Bills:\n")
                    with open("bill_history.txt", "r") as f:
                        print(f.read())
                    input("Press Enter to return to the Admin Portal menu...")
                else:
                    print("No bills found yet.")
                    input("Press Enter to return to the Admin Portal menu...")

            elif choice == "2":
                if os.path.exists("bill_history.txt"):
                    total = 0
                    today = datetime.now().strftime("%d-%m-%Y")
                    with open("bill_history.txt", "r") as f:
                        add_bill = False
                        for line in f:
                            if line.startswith("Order Time:"):
                                add_bill = today in line
                            if add_bill and line.startswith("Total Amount to Pay:"):
                                amount = float(line.strip().split(": Rs. ")[-1])
                                total += amount
                    print(f"\n💰 Total Sales Today ({today}): Rs. {total:.2f}")
                    input("Press Enter to return to the Admin Portal menu...")
                else:
                    print("No sales data available.")
                    input("Press Enter to return to the Admin Portal menu...")

            elif choice == "3":
                break
            elif choice == "4":
                print("Exiting...")
                exit()
            else:
                print("Invalid choice. Try again.")

    # Admin login
    is_admin = input("Are you the admin? (yes/no): ").strip().lower()
    if is_admin == "yes":
        admin_password = "cafe123"
        password = input("Enter admin password: ")
        if password != admin_password:
            print("Access Denied!")
            return
        else:
            admin_portal()

    print("Proceeding as guest...")

    # Customer details
    name = input("Enter customer name: ")
    print(f"Hello {name.upper()}!\n")
    order_time = datetime.now().strftime("%d-%m-%Y %H:%M")

    menu = {
        "Main Course": {"Paneer Butter Masala": 250, "Veg Biryani": 200, "Dal Makhani": 180},
        "Cold Coffee": {"Classic Cold Coffee": 120, "Mocha": 150, "Hazelnut Coffee": 170},
        "Sandwich": {"Cheese Sandwich": 100, "Veg Club Sandwich": 150, "Grilled Paneer Sandwich": 180},
        "Pizza": {"Margherita": 250, "Farmhouse": 300, "Peppy Paneer": 350}
    }

    total_bill = 0
    order = []

    print("\nWelcome to the Cafe! \nHere is our menu:")
    for category, items in menu.items():
        print(f"\n{category}:")
        for item, price in items.items():
            print(f"  {item} - Rs. {price}")

    while True:
        print("\nChoose a category:")
        for i, category in enumerate(menu.keys(), 1):
            print(f"{i}. {category}")
        print("5. Exit & Generate Bill")

        try:
            choice = int(input("Enter your choice (1-5): "))
            if choice == 5:
                break

            if choice < 1 or choice > 4:
                print("Invalid category choice. Try again.")
                continue

            category_name = list(menu.keys())[choice - 1]
            print(f"\nYou chose {category_name}. Select an item:")

            items_list = list(menu[category_name].items())
            for j, (item, price) in enumerate(items_list, 1):
                print(f"{j}. {item} - Rs. {price}")

            try:
                item_choice = int(input(f"Enter your choice (1-{len(items_list)}): "))
                if item_choice < 1 or item_choice > len(items_list):
                    print("Invalid item choice. Try again.")
                    continue
                quantity = int(input("Enter quantity: "))
                if quantity <= 0:
                    print("Quantity must be positive. Try again.")
                    continue
                selected_item, item_price = items_list[item_choice - 1]
                order.append((selected_item, item_price, quantity))
                total_bill += item_price * quantity
                print(f"{selected_item} x{quantity} added to your order!")

            except ValueError:
                print("Please enter valid numbers for item and quantity.")
            except IndexError:
                print("Invalid item choice. Try again.")

        except ValueError:
            print("Please enter a valid number for category choice.")

    if not order:
        print("No items ordered. Exiting.")
        return

    gst = total_bill * 0.05
    discount = total_bill * 0.10 if total_bill >= 1000 else 0
    final_total = total_bill + gst - discount

    payment_method = ""
    while True:
        print("\nSelect Payment Method:")
        print("1. Cash\n2. Card\n3. UPI")
        payment_option = input("Enter choice (1/2/3): ")

        payment_modes = {"1": "Cash", "2": "Card", "3": "UPI"}
        payment_method = payment_modes.get(payment_option, "Unknown")

        if payment_option not in ["1", "2", "3"]:
            print("Invalid payment option. Try again.")
            continue

        if payment_option == "3":
            print("\nPlease scan this QR to pay via UPI (PhonePe):")

            upi_id = "anshv5837@ybl"  # Change to your actual UPI ID
            payee_name = "Ansh's Cafe"
            upi_data = f"upi://pay?pa={upi_id}&pn={payee_name}&am={final_total:.2f}&cu=INR"

            qr = qrcode.QRCode()
            qr.add_data(upi_data)
            qr.make()
            qr.print_ascii(invert=True)

            img = qr.make_image(fill_color="black", back_color="white")
            img.save("upi_payment_qr.png")
            try:
                if os.name == 'nt':
                    os.startfile("upi_payment_qr.png")
                else:
                    os.system("open upi_payment_qr.png")
            except:
                pass

            while True:
                confirm = input("\nIs payment completed? (yes/no): ").strip().lower()
                if confirm == "yes":
                    print("✅ Payment received.")
                    break
                elif confirm == "no":
                    print("🔁 Returning to payment options...")
                    break
                else:
                    print("Please type 'yes' or 'no'.")

            if confirm == "yes":
                break
        else:
            break

    # Print summary and save
    print("\n===== Cafe Order Summary =====")
    print(f"Customer Name: {name}")
    print(f"Order Time: {order_time}\n")
    for item, price, qty in order:
        print(f"{item} x{qty} = Rs. {price * qty}")
    print(f"\nSubtotal: Rs. {total_bill}")
    print(f"GST (5%): Rs. {gst:.2f}")
    if discount:
        print(f"Discount (10%): Rs. {discount:.2f}")
    print(f"Total Amount to Pay: Rs. {final_total:.2f}")
    print(f"Payment Method: {payment_method}")
    print("🧾 Thank you for visiting our cafe!\n")

    with open("bill.txt", "w") as f, open("bill_history.txt", "a") as history:
        for file in (f, history):
            file.write("===== Cafe Order Summary =====\n")
            file.write(f"Customer Name: {name}\n")
            file.write(f"Order Time: {order_time}\n\n")
            for item, price, qty in order:
                file.write(f"{item} x{qty} = Rs. {price * qty}\n")
            file.write(f"\nSubtotal: Rs. {total_bill}\n")
            file.write(f"GST (5%): Rs. {gst:.2f}\n")
            if discount > 0:
                file.write(f"Discount (10%): Rs. {discount:.2f}\n")
            file.write(f"Total Amount to Pay: Rs. {final_total:.2f}\n")
            file.write(f"Payment Method: {payment_method}\n")
            file.write("Thank you for visiting our cafe!\n\n")

if __name__ == "__main__":
    cafe_management()
