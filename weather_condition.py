is_hot = input("Is it hot? (yes/no): ").lower() == "yes"
is_cold = input("Is it cold? (yes/no): ").lower() == "yes"

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")

print("Enjoy your day!")
