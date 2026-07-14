# Problem 1
number_of_tries = 1
favorite_color = input(
    "What is your favorite primary color: red, yellow, or blue?\n"
).lower()

while favorite_color not in ("red", "yellow", "blue"):
    number_of_tries += 1
    favorite_color = input(
        "That is not a primary color. What is your favorite primary color?\n"
    ).lower()

print(f"You chose {favorite_color} after {number_of_tries} tries.")

# Problem 2
first_integer = int(input("Enter an integer:\n"))
second_integer = int(input("Enter another integer\n"))
even_number_sum = 0

for number in range(first_integer, second_integer + 1):
    if number % 2 == 0:
        even_number_sum += number

print(
    f"The sum of the even numbers in the range "
    f"[{first_integer}, {second_integer}] is {even_number_sum}"
)

# Problem 3
user_string = input("Enter a string:\n")
vowel_count = 0

for character in user_string:
    if character.lower() in "aeiou":
        vowel_count += 1

print(f'"{user_string}" contains {vowel_count} vowels')
