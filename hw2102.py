import random

#задаю величину массива
array_size = 333

#делаю массив рандомных целых чисел от 1 до 1000
random_number = [random.randint(1, 1000) for _ in range(array_size)]

#просто для проверки
#print(random_number)

#создаю инпут для пользователя
guess = int(input("Enter a number from 1 to 1000:"))

#задаю условия, если введенное число есть в массиве и если нет
if guess in random_number:
    print("The number is in the array")
else:
    print("The number isn't in the array")