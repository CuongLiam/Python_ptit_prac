def my_func(a, b):

    result = max(a, b)

    return result

print(my_func(2, 100))


# dictionary

d = {"USD": {
    "mua": 25720,
    "ban": 26110
}}

print(d["USD"]["mua"])

# FILE HANDLING

with open("my_text.txt", "r", encoding="utf8") as f:
    text = f.read()
words = text.split()

print(words)

while True:
    print("1. Do A")
    print("2. Do B")
    print("0. Exit")
    choice = input("Choice: ")

    if choice == "1":
        # call function
        print("hi")
    elif choice == "0":
        break
