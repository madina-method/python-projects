import random

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

random.shuffle(numbers) # перемешиваем массив

computer_number = ""


for i in range(2, 5):
    computer_number = computer_number + str(numbers[i])

tries = 7 # количество попыток
while tries>0:
    keywords = [] # обнуляем массив ключевых слов
    my_number = input("Guess my number: ")

    if my_number == computer_number:
        print("You won!")
        break
    else:
        for i in range(3):
            if my_number[i] == computer_number[i]:
                keywords.append("Byk") # append добавить в конец
            elif my_number[i] in computer_number:
                keywords.append("Korova")

    print(keywords) # показываем ключевые слова
    tries = tries - 1 # уменьшаем попытки

if tries == 0: # если закончились попытки
    print("You lost! My number was", computer_number)
                
# length of me == 3
# number of tries
