from random import randint

while True:
    try:
        min_num = int(input("От какого числа вы загадали?: "))
        max_num = int(input("До какого числа вы загадали?: "))
        if min_num <= max_num:
            break
        else:
            print("Начальное число не может быть больше конечного. Попробуйте снова.")
    except ValueError:
        print("Введите корректное числовое значение.")

random_number = randint(min_num, max_num)

print(f"\nЗагадайте число от {min_num} до {max_num}. Я попытаюсь его угадать.")

low = min_num
high = max_num
attempts = 0

while True:
    attempts += 1
    guess = (low + high) // 2
    print(f"Мое предположение: {guess}")

    while True:
        hint = input("Ваше число больше (б), меньше (м) или равно (р) моему предположению? ").lower()
        if hint in ('б', 'м', 'р'):
            break
        else:
            print("Пожалуйста, введите 'б' (больше), 'м' (меньше) или 'р' (равно).")

    if hint == 'р':
        print(f"Ура! Я угадал ваше число {guess} за {attempts} попыток!")
        break
    elif hint == 'б':
        low = guess + 1
        if low > high:
            print("Что-то пошло не так. Возможно, вы допустили ошибку при ответах.")
            break
    else:  # hint == 'м'
        high = guess - 1
        if low > high:
            print("Что-то пошло не так. Возможно, вы допустили ошибку при ответах.")
            break
