# coding exercise 1

while True:
    user_country = input("Country of origin: ")
    user_country = user_country.upper()

    match user_country:
        case 'USA':
            print("Hello")

        case 'INDIA':
            print("Namaste")

        case 'GERMANY':
            print("Hallo")

# coding exercise 2
# write a for-loop below that line that makes the program produce the following output:

# ingredients = ["john smith", "sen plakay", "dora ngacely"]
#
# for ingredient in ingredients:
#     print(ingredient.title())
