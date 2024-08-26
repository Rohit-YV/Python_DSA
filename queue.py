queue=[]

def enqueue():
    element=input("enter the element you want to inserted")
    queue.append(element)
    print(element,"is interted")

def dequeue():
    if not queue:
        print("queue is empty")
    else:
        e=queue.pop(0)
        print(e,"is removed")

def display():
    if not queue:
        print("queue is empty")

    else:
        print(queue)

while True:
    print("enter operation press 1.add_element 2.remove_element 3.display")
    choice=int(input("enter  your choice "))
    if choice==1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice==3:
        display()
    elif choice ==4:
        break
    else:
        print("please enter a valid choice")
