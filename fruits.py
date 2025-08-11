fruit_prices = {
    "apple": 120,
    "banana": 40,
    "orange": 80,
    "mango": 150,
    "grapes": 100,
    "pineapple": 90,
    "watermelon": 30,
    "kiwi": 200,
    "papaya": 60,


    -"pomegranate": 140
}
cart = {}
total_bill = 0

print("🛍️ Welcome to the Fruit Shop!")
print("\nAvailable Fruits (Price per kg):")
print("-----------------------------------")
for i, (fruit, price) in enumerate(fruit_prices.items(), 1):
    print(f"{i}. {fruit.title()} - ₹{price}/kg")
print("-----------------------------------")

while True:
    choice = input("\nEnter the name of the fruit to buy (or type 'done' to finish): ").lower() if choice == 'done':
        break
    if choice in fruit_prices:
        qty = float(input(f"How many kg of {choice}? "))
        cost = qty * fruit_prices[choice]
        cart[choice] = {'price_per_kg': fruit_prices[choice], 'qty': qty, 'cost': cost}
        total_bill += cost
    else:
        print("❌ Fruit not in the list. Please select from available options.")
        print("\n🧾 FINAL BILL")
print("-----------------------------------")
for fruit, info in cart.items():
    print(f"{fruit.title()} - ₹{info['price_per_kg']}/kg x {info['qty']}kg = ₹{info['cost']:.2f}")
print("-----------------------------------")
print(f"Total Amount to Pay: ₹{total_bill:.2f}")
