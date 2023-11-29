'''
	FIFO - insert() and pop()

	Operations of Queue
		a. enqueue() 	- to insert
			Steps:
				1. Check if the queue is full or not
					1.1. If full, print "Overflow" and end the operation.
					1.2. If not full, proceed to Step 2.
				2. Increment the tail.
				3. Add the element.
		b. dequeue() 	- to remove
		c. front()
		d. rear()		- to check
		e. isEmpty()	- to know if queue is empty or not
		f. isFull()		- to know if queue is full or not
		g. size()		- capacity of the queue
'''


class Queue:
    def __init__(self, capacity):
        self.front = self.size = 0
        self.rear = capacity - 1
        self.QList = [None] * capacity
        self.capacity = capacity

    def isFull(self):
        return self.size == self.capacity

    def isEmpty(self):
        return self.size == 0

    def enqueue(self, item):
        if self.isFull():
            print("The list is full or overflow.")
            return
        self.rear = (self.rear + 1) % (self.capacity)
        self.QList[self.rear] = item
        self.size = self.size + 1
        print("'%s' added to list." % str(item))

    def queueFront(self):
        if self.isEmpty():
            print("Queue is empty.")
        print("Front item: ", self.QList[self.front])

    def queueRear(self):
        if self.isEmpty():
            print("Queue is empty.")
        print("Rear item: ", self.QList[self.rear])

    def dequeue(self):
        # If Queue is empty, print a status message and skip the succeeding code
        if self.isEmpty():
            print("Queue is empty.")
            return
        # Store the original element in the front in a temporary variable named "dequeued".
        dequeued = self.QList[self.front]
        # Set the value of the front element to "None", manually removing the element
        self.QList[self.front] = None
        # Increment the index of the front by 1, but use modulo so that the index only circulates until the value of the capacity
        # capacity = 4 | self.front = 0(0) -> 1(1) -> 2(2) -> 3(3) -> 4(4) -> 0(5) -> 1(6) -> 2(7) -> 3(8) -> 4(9) -> ...
        self.front = (self.front + 1) % (self.capacity)
        # Decrement the size of the Queue as an element is manually removed
        self.size = self.size - 1
        # Print the dequeued element.
        print("'%s' dequeued from Queue." % str(dequeued))


if __name__ == '__main__':
    queue = Queue(5)

    while True:
        option = input("Add or Remove vehicle? [add/remove/done]: ")
        print("~~~~~~~~~~~~~~~~~~~~~")
        if option.lower() == "add":
            y = input("Add plate number: ")
            queue.enqueue(y)
            print("===============")
            queue.queueFront()
            queue.queueRear()
            print("===============")
            print("\n")
        elif option.lower() == "remove":
            queue.dequeue()
            print("===============")
            queue.queueFront()
            queue.queueRear()
            print("===============")
            print("\n")
        else:
            print("Thank you!")
            break

        choice = input("Do you still want to add?: ")
        if choice.lower() == "yes":
            continue
        elif choice.lower() == "no":
            continue
        else:
            break