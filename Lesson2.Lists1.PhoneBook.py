import time

spisok = ["Madina", "Amina", "Islam"]

while True:
    print("\n1. Add student")
    print("2. Delete student")
    print("3. Edit student")
    print("4. Search student")
    print("5. Show all students")
    print("6. Exit\n")

    punkt = int(input("Choose: \n"))

    if punkt == 1:
        name = input("Enter the name: ")
        spisok.append(name)
    elif punkt == 2:
        name = input("Enter the name to delete: ")
        # flags
        a = 0
        for i in range(0, len(spisok)): 
            if spisok[i] == name:
                a = 1
                del spisok[i]
                break
        if a==0:
            print("\nNo such student")




    elif punkt == 3:
        name = input("Enter the name to edit: ")
        newname = input("Enter new name: ")

        a = 0
        for i in range(0, len(spisok)): 
            if spisok[i] == name:
                a = 1
                spisok[i] = newname
                
                break
        if a==0:
            print("No such student")


            
    elif punkt == 4:
        name = input("Enter the name to search: ")
        a = 0
        for i in range(0, len(spisok)): 
            if spisok[i] == name:
                a = 1
                print("Here it is!")
                break
        if a==0:
            print("No such student") 


    elif punkt == 5:
        for i in range(0, len(spisok)):
            print(spisok[i])

    elif punkt == 6:
        print("Bye!")
        break

    else:
        print("R u stupid??")
    
    time.sleep(3)
            


# добавить нумерацию в 5-ом пункте
# добавить флажки в 1-ом пункте




        
    
