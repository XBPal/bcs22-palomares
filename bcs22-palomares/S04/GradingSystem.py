passed = 0
failed = 0
record = [["Name", "Q1", "Q2", "Q3", "Class Participation", "Final Exam", "Grade", "Status"]]

while True:
    n = input("Enter Student's Name: ")
    q1 = int(input("Enter 1st Quarter Grade: "))
    q2 = int(input("Enter 2nd Quarter Grade: "))
    q3 = int(input("Enter 3rd Quarter Grade: "))
    cp = int(input("Enter Class Participation: "))
    f_E = int(input("Enter Final Exam Grade: "))

    qTotal = (q1 + q2 + q3)/3
    fG = (qTotal * .4) + (cp * .2) + (f_E * .4)

    if fG >= 75:
        status = "Passed"
    else:
        status = "Failed"

    g = f"{fG:.1f}"

    s_Record = [n, q1, q2, q3, cp, f_E, g, status]

    record.append(s_Record)

    new = input("Do you want to enter another student (Yes or No): ").lower()

    if new == "yes":
        continue
    elif new == "no":
        break
    else:
        print("Invalid Input")

for column in range(len(record)):
    display = "| {0:^7} | {1:^7} | {2:^7} | {3:^7} | {4:^7} | {5:^10} | {6:^7} | {7:^9} |"
    print(display.format((record[column][0]), (record[column][1]), (record[column][2]), (record[column][3]), (record[column][4]), (record[column][5]), (record[column][6]), (record[column][7])))

for column in range(len(record)):
    if record[column][7].lower() == "passed":
        passed =+ 1
    else:
        continue

print("********************************************************************************************")
print(f"There are {passed} students who passed the Midterm Period")
print(f"There are {failed} students who failed the Midterm Period")
print("********************************************************************************************")