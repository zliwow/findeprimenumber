your_number = input("enter a number")
num = int(your_number)

if num < 2:
    print("not prime")
    quit()

for i in range(2, num):
    if num % i == 0:
        print("not prime")
        quit()

print("is prime")