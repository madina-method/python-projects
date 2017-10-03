import time

contacts = {"Madina":"87654321", "Zhalgas":"12345678"}

"""
print(slovar["dog"])
slovar["cow"] = "корова" # adding editing
print(slovar)

find = input("Что хочешь найти? ")

if find in slovar:
    print(slovar["cat"])
else:
    print("Нет такого слова")

for key in slovar:
    print(key, "-", slovar[key])
"""

while True:

    print("\n1. Add contact")
    print("2. Edit contact")
    print("3. Delete contact")
    print("4. Search contact")
    print("5. Show all")
    print("6. Exit")

    vybor = int(input("\nWhat do you want to do?\n"))

    if vybor == 1:
        name = input("Name: ")
        if name in contacts: # если есть такой ключ (работает как for)
            print("Already exists")
        else:
            tel = input("Telephone: ")
            contacts[name] = tel
           

    elif vybor == 2:
        name = input("Name: ")
        if name in contacts: # если есть такой ключ (работает как for)
            tel = input("Telephone: ")
            contacts[name] = tel
            
        else:
            print("No such contact")

    elif vybor == 3:
        name = input("Name: ")
        if name in contacts: # если есть такой ключ (работает как for)
            del contacts[name]
            
        else:
            print("No such contact")

    elif vybor == 4:
        name = input("Name: ")
        if name in contacts: # если есть такой ключ (работает как for)
            print(contacts[name])
        else:
            print("No such contact")

    elif vybor == 5:
        i = 1
        for name in contacts:
            print(i, name, "-", contacts[name])
            i+=1
        time.sleep(2)

    elif vybor == 6:
        print("Bye!")
        break

    else:
        print("No such number in menu")
        time.sleep(2)
    





        





