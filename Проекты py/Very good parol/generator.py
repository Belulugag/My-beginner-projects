# generator.py
import random
import string

# Функция генерации пароля
def generatepassword(use_lowercase, count_lowercase, use_uppercase, count_uppercase, use_numbers, count_numbers, use_special, count_special, total_length):
    """
    Генерирует пароль на основе заданных параметров.

    Args:
        use_lowercase (bool): Использовать ли строчные буквы.
        count_lowercase (int): Количество строчных букв.
        use_uppercase (bool): Использовать ли заглавные буквы.
        count_uppercase (int): Количество заглавных букв.
        use_numbers (bool): Использовать ли цифры.
        count_numbers (int): Количество цифр.
        use_special (bool): Использовать ли специальные символы.
        count_special (int): Количество специальных символов.
        total_length (int): Общая желаемая длина пароля.

    Returns:
        str: Сгенерированный пароль, или сообщение об ошибке.
    """

    # Проверка, выбраны ли хоть какие-то типы символов
    if not (use_lowercase or use_uppercase or use_numbers or use_special):
        return "Выберите хотя бы один тип символов."

    # Проверка, не превышает ли суммарное количество символов общую длину
    if (count_lowercase + count_uppercase + count_numbers + count_special) > total_length:
        return "Суммарное количество символов превышает общую длину."

    # Формирование набора символов для пароля
    password_chars = []
    types_to_use = []

    if use_lowercase:
        password_chars.extend(random.sample(string.ascii_lowercase, min(count_lowercase, total_length)))
        types_to_use.append(string.ascii_lowercase)
    if use_uppercase:
        password_chars.extend(random.sample(string.ascii_uppercase, min(count_uppercase, total_length)))
        types_to_use.append(string.ascii_uppercase)
    if use_numbers:
        password_chars.extend(random.sample(string.digits, min(count_numbers, total_length)))
        types_to_use.append(string.digits)
    if use_special:
        special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        password_chars.extend(random.sample(special_chars, min(count_special, total_length)))
        types_to_use.append(special_chars)

    # Дополнение пароля до общей длины, если необходимо
    remaining_length = total_length - len(password_chars)
    if remaining_length > 0 and types_to_use:
        full_char_set = "".join(types_to_use)
        password_chars.extend(random.choice(full_char_set) for _ in range(remaining_length))

    # Перемешивание символов в пароле
    random.shuffle(password_chars)

    return "".join(password_chars)
