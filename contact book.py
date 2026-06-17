a={}
def add(a):
    b=input("Enter name:")
    c=int(input("Enter phone number:"))
    a[b]=c
    print("Contact added successfully!")

def view(a):
    if len(a)!=0:
        print("----- Contact List -----")
        print()
        for i,j in a.items():
            print(i,":",j)
    else:
        print("No contacts found.")

def search(a):
    d=input("Enter name:")
    if d in a:
        print("Contact Found")
        print()
        print("Name :",d)
        print("Phone :",a[d])
    else:
        print("Contact not found.")
        
def delete(a):
    e=input("Enter name:")
    if e in a:
        a.pop(e)
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def ex(a):
    print("Thank you for using Contact Book.")

while True:
    print("===== Contact Book =====")
    print()
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    print()
    f=int(input("Enter choice:"))
    if f==1:
        add(a)
    elif f==2:
        view(a)
    elif f==3:
        search(a)
    elif f==4:
        delete(a)
    elif f==5:
        ex(a)
        break
    else:
        print("Enter valid choice")




        







            
        
    
