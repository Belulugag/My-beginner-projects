import tkinter as tk
from tkinter import Tk, LabelFrame, Checkbutton, Button, Entry, BooleanVar

import generator

tk_main = Tk()
tk_main.title("Генератор Паролей")
tk_main.geometry("400x450")

main_frame = tk.Frame(tk_main, padx=10, pady=10)
main_frame.pack(expand=True, fill="both")

t1_main = LabelFrame(main_frame, text="Параметры пароля", padx=10, pady=10)
t1_main.pack(pady=20, padx=20, fill="x")

lowercase_var = tk.BooleanVar()
uppercase_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
special_chars_var = tk.BooleanVar()

cb_lowercase = Checkbutton(t1_main, text="Строчные буквы (a-z)", variable=lowercase_var, onvalue=True, offvalue=False)
cb_lowercase.pack(anchor='w', pady=2, padx=10)
lowercase_var.set(True)

cb_uppercase = Checkbutton(t1_main, text="Заглавные буквы (A-Z)", variable=uppercase_var, onvalue=True, offvalue=False)
cb_uppercase.pack(anchor='w', pady=2, padx=10)
uppercase_var.set(True)

cb_numbers = Checkbutton(t1_main, text="Цифры (0-9)", variable=numbers_var, onvalue=True, offvalue=False)
cb_numbers.pack(anchor='w', pady=2, padx=10)
numbers_var.set(True)

cb_special = Checkbutton(t1_main, text="Спец. символы (!@#$)", variable=special_chars_var, onvalue=True, offvalue=False)
cb_special.pack(anchor='w', pady=2, padx=10)

length_frame = tk.Frame(t1_main)
length_frame.pack(pady=10, padx=10, fill="x")

tk.Label(length_frame, text="Длина пароля:").pack(side=tk.LEFT, padx=5)

entry_length = Entry(length_frame, width=5)
entry_length.pack(side=tk.LEFT, padx=5)
entry_length.insert(0, "12")
tk.Label(length_frame, text="символов").pack(side=tk.LEFT, padx=5)


def generate_password_action():
    use_lowercase = lowercase_var.get()
    use_uppercase = uppercase_var.get()
    use_numbers = numbers_var.get()
    use_special = special_chars_var.get()

    try:
        length = int(entry_length.get())
        if length <= 0:
            result_entry.delete(0, 'end')
            result_entry.insert(0, "Длина должна быть > 0")
            return
    except ValueError:
        result_entry.delete(0, 'end')
        result_entry.insert(0, "Некорректная длина")
        return

    if not (use_lowercase or use_uppercase or use_numbers or use_special):
        result_entry.delete(0, 'end')
        result_entry.insert(0, "Выберите хотя бы один тип символов")
        return

    password = generator.generatepassword(
        use_lowercase, use_uppercase, use_numbers, use_special, length
    )

    result_entry.delete(0, 'end')
    result_entry.insert(0, password)

generate_button = Button(main_frame, text="Сгенерировать пароль", command=generate_password_action, font=('Arial', 12, 'bold'))
generate_button.pack(pady=15, padx=20, fill="x")

result_frame = tk.Frame(main_frame)
result_frame.pack(pady=10, padx=20, fill="x")

tk.Label(result_frame, text="Ваш пароль:").pack(side=tk.LEFT, padx=5)
result_entry = Entry(result_frame, width=30, font=('Courier New', 12))
result_entry.pack(side=tk.LEFT, fill="x", expand=True, padx=5)


if __name__ == "__main__":
    tk_main.mainloop()
