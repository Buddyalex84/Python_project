admin_password = "cafe123"
password = input("Enter admin password to start: ")
if password != admin_password:
    print("Access Denied!")
    exit()

from datetime import datetime

name = input("Enter customer name: ")
order_time = datetime.now().strftime("%d-%m-%Y %H:%M")
print(f"Order time: {order_time}")
print(f"Customer name: {name}")

order.append((selected_item, item_price))



