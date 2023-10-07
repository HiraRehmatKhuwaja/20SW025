# -*- coding: utf-8 -*-
"""20SW025

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GuITVVKAOEU2Uvw_90nJ73fZe52UDmcr
"""

answer = 42  # Replace 42 with your chosen number
guess = int(input("Enter your guess: "))  # Assuming the user's guess is provided through input

if guess < answer:
    result = "Oops! Your guess was too low."
elif guess > answer:
    result = "Oops! Your guess was too high."
else:
    result = "Nice! Your guess matched the answer!"

print(result)

def calculate_total_purchase(amount, state):
    # Define a dictionary to store the tax rates for each state
    state_tax_rates = {
        'CA': 0.075,  # 7.5% tax rate for California
        'MN': 0.095,  # 9.5% tax rate for Minnesota
        'NY': 0.089,  # 8.9% tax rate for New York
    }

    # Check if the state provided is valid (exists in the state_tax_rates dictionary)
    if state in state_tax_rates:
        # Calculate the tax amount based on the tax rate for the given state
        tax_rate = state_tax_rates[state]
        tax_amount = amount * tax_rate

        # Calculate the total amount after applying tax
        total_amount = amount + tax_amount

        return total_amount
    else:
        # If the state is not valid, return an error message
        return "Error: Invalid state provided. Please enter a valid state (CA, MN, or NY)."

# Example usage:
amount_of_purchase = 100.00
state_of_purchase = "CA"

total_purchase_amount = calculate_total_purchase(amount_of_purchase, state_of_purchase)
print(f"Total purchase amount with tax: ${total_purchase_amount:.2f}")

sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]

for word in sentence:
    print(word)

for number in range(5, 31, 5):
    print(number)

names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

# List comprehension to extract the first names in lowercase
first_names = [name.split()[0].lower() for name in names]

print(first_names)

scores = {
    "Rick Sanchez": 70,
    "Morty Smith": 35,
    "Summer Smith": 82,
    "Jerry Smith": 23,
    "Beth Smith": 98
}

# List comprehension to filter names with scores of at least 65
passed = [name for name, score in scores.items() if score >= 65]

print(passed)

cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]
cast = dict(zip(cast_names, cast_heights))
print(cast)

cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

# Modify the cast list to include names and heights
for index, name in enumerate(cast):
    cast[index] = f"{name} {heights[index]}"

print(cast)

prize = int(input())

if prize >= 1 and prize <= 50:
    print('Congratulations!!!! Wooden rabbit')
elif prize > 50 and prize <= 150:
    print('Alasss!!!! No prize')
elif prize > 150 and prize <= 180:
    print('Congratulations!!!! Wafer-thin mint')
elif prize > 180 and prize <= 200:
    print('Congratulations!!!! Penguin')
else:
    print('Ooh dear!!! No prize this time')