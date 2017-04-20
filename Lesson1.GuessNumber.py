import random # загружаем модуль random

comp = random.randint(1, 10) # генерируем число от 1 до 10

p = 5 # количество попыток


while p>0: # цикл, до тех пор пока попытки больше 0-ля 

    me = int(input("Guess my number: ")) # прога спрашивает число

    if me == comp: # условие, если угадали число
        print("You won!")
        break #
    elif me>comp: # условие, число юзера больше чем у компа
        print("Less")
    else: # условие, число юзера меньше чем у компа
        print("Bigger")
    p = p - 1 # уменьшаем попытки на 1

if p==0: # условие, если закончились попытки
    print("You lost! My number was", comp)

# asks name user
# check if in range
# show tries



