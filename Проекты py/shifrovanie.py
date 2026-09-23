from tkinter import *

# Функция шифрования/дешифрования Цезаря
def caesar_cipher(text, shift, mode):
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            start = ord('a')
            new_ord = (ord(char) - start + shift * mode) % 26 + start
            result.append(chr(new_ord))
        elif 'A' <= char <= 'Z':
            start = ord('A')
            new_ord = (ord(char) - start + shift * mode) % 26 + start
            result.append(chr(new_ord))
        else:
            result.append(char)
    return "".join(result)

# Функция шифрования/дешифрования Атбаш
def atbash_cipher(text):
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            result.append(chr(ord('a') + (ord('z') - ord(char))))
        elif 'A' <= char <= 'Z':
            result.append(chr(ord('A') + (ord('Z') - ord(char))))
        else:
            result.append(char)
    return "".join(result)

# Окно приложения
tk = Tk()
tk.geometry("400x500")
tk.title("Шифровальщик")

# Связки для выбора шифра
cipher_type = StringVar()
cipher_type.set("caesar")  # Шифр Цезаря по умолчанию

# Элементы интерфейса
c_caesar = Radiobutton(tk, text="Шифр Цезаря", variable=cipher_type, value="caesar")
c_atbash = Radiobutton(tk, text="Шифр Атбаш", variable=cipher_type, value="atbash")

tk.label_shift = Label(tk, text="Сдвиг (для Цезаря):")
tk.entry_shift = Entry(tk, width=5)
tk.entry_shift.insert(0, "3")  #  Значение сдвига по умолчанию

tk.label_input = Label(tk, text="Введите текст:")
tk.entry_input = Entry(tk, width=30)

tk.button_process = Button(tk, text="Обработать", height=1, width=10)
tk.label_result = Label(tk, text="", wraplength=350) # Раздел для вывода результата

# Размещение элементов на окне
c_caesar.pack(pady=5)
c_atbash.pack(pady=5)
tk.label_shift.pack(pady=5)
tk.entry_shift.pack(pady=5)
tk.label_input.pack(pady=5)
tk.entry_input.pack(pady=5)
tk.button_process.pack(pady=10)
tk.label_result.pack(pady=10)

# Обработчик нажатия кнопки
def process_text():
    text = tk.entry_input.get() # Получаем текст из поля ввода
    cipher = cipher_type.get()   # Определяем выбранный шифр
    result_label_text = ""

    if cipher == "caesar":
        try:
            shift = int(tk.entry_shift.get()) # Получаем значение сдвига
            # Шифруем и дешифруем сдвигом
            encrypted_caesar = caesar_cipher(text, shift, 1)
            decrypted_caesar = caesar_cipher(text, shift, -1)
            result_label_text = f"Цезарь:\nЗашифровано: {encrypted_caesar}\nДешифровано: {decrypted_caesar}"
        except ValueError:
            result_label_text = "Введите корректное число для сдвига."
    elif cipher == "atbash":
        # Шифруем и дешифруем Атбаш (одинаковая операция)
        processed_atbash = atbash_cipher(text)
        result_label_text = f"Атбаш:\nОбработано: {processed_atbash}"

    tk.label_result.config(text=result_label_text) # Обновляем текст в метке результата

# Привязка функции к кнопке
tk.button_process.config(command=process_text)

tk.mainloop() # Запуск главного цикла окна
