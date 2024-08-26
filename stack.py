stack=[]
def push():
    element = input("enter the element you want to insert")
    stack.append(element)
    print(stack)

def pop():
    if not stack:
        print("stack is empty")
    else:
        e=stack.pop()
        print(stack)

def display():
    if not stack:
        print("stack is empty")
    else:
        print(stack)

while True:
    print("select the operation 1.push 2.pop 3.display 4.quit")
    choice = int(input())
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("enter a correct operation value")