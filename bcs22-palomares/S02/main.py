service = str=input("Enter your years of service: ")
salary = int(input("Enter your Salary($): "))

if service == '5':
    bonus = (salary * .05)
    totalAmount = (bonus + salary)
    rTime = 1
    print(f"Your bonus is ${bonus},\nYour total salary should be ${totalAmount}")
    print(f"Running Time: {rTime}(n)")
elif service == '10':
    bonus = (salary * 1)
    totalAmount = (bonus + salary)
    rTime = 2
    print(f"Your bonus is ${bonus},\nYour total salary should be ${totalAmount}")
    print(f"Running Time: {rTime}(n)")
elif service == '15':
    bonus = (salary * 1.5)
    totalAmount = (bonus + salary)
    rTime = 3
    print(f"Your bonus is ${bonus},\nYour total salary should be ${totalAmount}")
    print(f"Running Time: {rTime}(n)")
elif service == '20':
    bonus = (salary * 2)
    totalAmount = (bonus + salary)
    rTime = 4
    print(f"Your bonus is ${bonus},\nYour total salary should be ${totalAmount}")
    print(f"Running Time: {rTime}(n)")
else:
    rTime = 5
    print("You don't have any bonus")
    print(f"Running time complexity: {rTime}(n)")