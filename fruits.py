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
    "pomegranate": 140
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
    choice = input("\nEnter the name of the fruit to buy (or type 'done' to finish): ").lower()
