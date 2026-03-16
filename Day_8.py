# Enter your code here. Read input from STDIN. Print output to STDOUT 

a = int(input("Enter the number of entries: ").strip())
phone_book = {}

for x in range(a):
    key, value = input("Enter name and phone number: ").split()
    phone_book[key] = value

while True:
    try:
        key1 = input("Enter name to search: ").strip()
        if key1 in phone_book:
            print(f"{key1}={phone_book[key1]}")
        else:
            print("Not found")
    except EOFError:
        break

