import time

# Node class for the linked list
class Node:
	def __init__(self, x):
		self.data = x
		self.next = None

#Stack class for linked list
class Stack:
    def __init__(self):
        self.top = None

    def push(self, x):
        new = Node(x)

        if self.top is None:
            self.top = new
            self.top.next = None
        else:
            new.next = self.top
            self.top = new

    def pop(self):
        if self.top is None:
            print("Stack is empty")
        elif self.top.next is None:
            print(f"Popped Element is : {self.top.data}")
            print("=====================================")
            self.top = None
        else:
            temp = self.top
            print(f"Popped Element is : {self.top.data}")
            print("=====================================")
            self.top = temp.next
            temp = None

    def getlist(self):
        if self.top is None:
            print("Stack is Empty")
        else:
            reversedList = []
            temp = self.top
            while temp:
                reversedList.append(temp.data)
                temp = temp.next
            return reversedList

# Palindrome checker function
def palindrome(palinInput):
    print("Checking stored data...")
    time.sleep(2)

    check = palinInput.lower()
    checklist = []
    reverseStack = Stack()

    for character in check:
        if character.isalpha():
            checklist.append(character)
            reverseStack.push(character)

    reverseList = reverseStack.getlist()
    correct = "".join(checklist)
    reverse = "".join(reverseList)

    print("Palindrome Checker")
    print("========================")
    print(f"Entered: {palinInput}")
    print(f"Checked: {correct}")
    print(f"Reversed: {reverse}")
    print("========================")

    if correct == reverse:
        print("Valid Palindrome")
    else:
        print("Not a Palindrome")
    print("=============================")

# User input palindrome function
while True:
    checker = input("Enter input: ")
    palindrome(checker)

    restart = input("Check another? ")

    if restart.lower() == "yes":
        continue
    elif restart.lower() == "no":
        print("Thank you for using Palindrome Checker!")
        break
    else:
        print("Invalid input. Thank you for using Palindorme Checker!")


# Reflection: Though stacking numbers is fairly simple, stacking letters is more tough for me, especially in this
# activity. Still, it amuses me that we can stack letters similarly to numbers.

