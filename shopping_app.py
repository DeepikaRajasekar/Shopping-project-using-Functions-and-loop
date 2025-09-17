products= {1:{"name":"laptop","price":50000},2:{"name":"smartphone","price":70000},3:{"name":"headphones","price":1500},4:{"name":"Tv","price":30000},5:{"name":"table","price":10000}}
cart=[]
def show_menu():
    print("\n==== SHOPPING APP====")
    print("1. View products")
    print("2. Add to cart")
    print("3. View cart")
    print("4. Checkout")
    print("5. Exit")
while True:
    show_menu()
    choices=input("enter the choices (1-5):")
    if choices=="1":
        print("/n Available Products")
        for pid,details in products.items():
            print(f"{pid}.{details['name']}- Rs.{details['price']}")
    elif choices=="2":
        pid=int(input("enter product Id to add to cart:"))
        if pid in products:
            cart.append(products[pid])
            print(f"{products[pid]['name']} added to cart")
        else:
            print("invalid product id")
    elif choices=="3":
        if not cart:
            print("your cart is empty")
        else:
            print("\n your cart:")
            total=0
            for item in cart:
                print(f" -{item['name']} - Rs.{item['price']}")
                total+=item["price"]
            print(f"Total: Rs.{total}")
    elif choices=="4":
        if not cart:
            print("your cart is empty")
        else:
            total=sum(item["price"] for item in cart)
            print("\n===== CHECKOUT")
            for item in cart:
                print(f" - {item['name']}- Rs .{item['price']}")
            print("total bill:",total)
            print("thank you")
            cart.clear()
    elif choices=="5":
        print("exiting the shopping app.Goodbye")
        break
    else:
        print("invalid choice,please try again!")
        
