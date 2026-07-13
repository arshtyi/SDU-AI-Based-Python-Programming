# Values and Types
# print("Hello world!")
# print('Hello world!')
# print(Hello world!)  # SyntaxError
# print(type("Hello world!"))  # <class 'str'>
# print(type('Hello world!'))   # <class 'str'>
# print(type(Hello world!))     # SyntaxError

# Expressions and Types
# print(type(3 / 2), 3 / 2)        # float, 1.5
# print(type(3.0 / 1), 3.0 / 1)    # float, 3.0
# print(type("3/2"), "3/2")        # str, "3/2"
# print(type("3" / 2), "3" / 2)    # TypeError
# print(type(3 * 2), 3 * 2)        # int, 6
# print(type(3.0 * 2), 3.0 * 2)    # float, 6.0
# print(type("3*2"), "3*2")        # str, "3*2"
# print(type("3" * 2), "3" * 2)    # str, "33"

# Using Expressions, Problem 1
cecil_hours = 9
cecil_minutes = 27
cecil_sleep_seconds = (cecil_hours * 60 + cecil_minutes) * 60
print(f"1. Cecil slept for {cecil_sleep_seconds} seconds.")

# Using Expressions, Problem 2
your_hours = float(input("How many hours did you sleep last night? "))
your_sleep_seconds = your_hours * 60 * 60
if your_sleep_seconds > 0:
    ratio = cecil_sleep_seconds / your_sleep_seconds
    print(f"2. Cecil slept {ratio:.2f} times as long as you did.")
else:
    print("2. Your sleep time must be greater than zero.")
