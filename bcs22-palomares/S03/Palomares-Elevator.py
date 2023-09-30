import time

floors = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(floors)

x = int(input("Enter current floor: "))
f = int(input("Enter your destination: "))

for l in range(x+1, f+1):
    time.sleep(l)
    x = l
    print(x)

print("You are now at Level: ", f)
time.sleep(1)

c = input("Do you want to change your destination? [yes/no]: ").lower()

if c == "yes":
    f = int(input("Enter your destination: "))
    if f > x:
        for l in range(x+1, f+1):
            time.sleep(l)
            f = l
            print(f)
    elif f < x:
        while x > f:
            time.sleep(1)
            x = x - 1
            print(x)
elif c == "no":
    print("Have a Good Day!")

print ("Your are now at level: ",f)
print("Have a Good Day!")

time.sleep(1)