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
            popped = self.top.data
            self.top = None
            return popped
        else:
            temp = self.top
            popped = temp.data
            self.top = temp.next
            temp = None
            return popped



# Palindrome checker function
def palindrome(palinInput):
    print("Checking stored data...")
    time.sleep(2)

    check = palinInput.lower()
    checklist = []
    reverseStack = Stack()
    checkletter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for character in check:
        if character in checkletter:
            checklist.append(character)
            reverseStack.push(character)

    reverseList = []
    for character in range(len(checklist)):
        popped = reverseStack.pop()
        reverseList.append(popped)
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

