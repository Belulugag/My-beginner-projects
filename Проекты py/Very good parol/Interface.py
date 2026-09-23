# interface.py
import tkinter as tk
from tkinter import Tk, LabelFrame, Checkbutton, Button, Entry, BooleanVar, Spinbox
import generator

root = Tk()
root.title("Генератор Паролей")

main_frame = tk.Frame(root, padx=10, pady=10)
main_frame.pack(expand=True, fill="both")

params_frame = LabelFrame(main_frame, text="Параметры пароля", padx=10, pady=10)
params_frame.pack(pady=20, padx=20, fill="x")
use_lowercase_var = BooleanVar(value=True)
use_uppercase_var = BooleanVar(value=True)
use_numbers_var = BooleanVar(value=True)
use_special_var = BooleanVar(value=True)
vars_list = [
    (use_lowercase_var, "Строчные буквы (a-z)", "5"),
    (use_uppercase_var, "Заглавные буквы (A-Z)", "5"),
    (use_numbers_var, "Цифры (0-9)", "5"),
    (use_special_var, "Спец. символы (!@#$)", "2")
]

checkbuttons = []
spinboxes = []
for var, text, default_value in vars_list:
    # Чекбокс
    cb = Checkbutton(params_frame, text=text, variable=var, onvalue=True, offvalue=False)
    cb.pack(anchor='w', pady=2, padx=10)
    checkbuttons.append(cb)

    frame = tk.Frame(params_frame)
    frame.pack(pady=5, padx=10, fill="x")
    tk.Label(frame, text=f"Кол-во {text.split(' ')[0].lower()}:").pack(side=tk.LEFT, padx=5)

    # Spinbox, состояние которого зависит от чекбокса
    sb = Spinbox(frame, from_=0, to=50, width=5, state=('normal' if var.get() else 'disabled'))
    sb.pack(side=tk.LEFT, padx=5)
    sb.delete(0, tk.END)
    sb.insert(0, default_value)
    spinboxes.append(sb)
def update_spinbox_states():
    for i, (var, _, _) in enumerate(vars_list):
        spinboxes[i].config(state=('normal' if var.get() else 'disabled'))
for var, _, _ in vars_list:
    var.trace_add("write", lambda *args: update_spinbox_states())

# Вызов функции при старте для установки начальных состояний
update_spinbox_states()

length_frame = tk.Frame(params_frame)
length_frame.pack(pady=10, padx=10, fill="x")
tk.Label(length_frame, text="Общая длина пароля:").pack(side=tk.LEFT, padx=5)
entry_length = Entry(length_frame, width=5)
entry_length.pack(side=tk.LEFT, padx=5)
entry_length.insert(0, "20") # Значение по умолчанию

def generate_password_action():
    counts = [] # Список для хранения количеств символов
    try:
        total_length = int(entry_length.get())
        if total_length <= 0: raise ValueError("Длина должна быть > 0")

        for i, (var_obj, _, _) in enumerate(vars_list):
            if var_obj.get(): 
                count = int(spinboxes[i].get())
                if count < 0: raise ValueError("Количество не может быть отрицательным")
                counts.append(count) 
            else:
                counts.append(0) 

        if total_length < sum(counts): raise ValueError("Кол-во символов > общей длины")
        if not any(var_obj.get() for var_obj, _, _ in vars_list): raise ValueError("Выберите тип символов")

    except ValueError as e: 
        result_entry.delete(0, 'end'); result_entry.insert(0, str(e))
        return

    password = generator.generatepassword(
        use_lowercase_var.get(), counts[0],
        use_uppercase_var.get(), counts[1],
        use_numbers_var.get(), counts[2],
        use_special_var.get(), counts[3],
        total_length # Передаем общий параметр длины
    )

    result_entry.delete(0, 'end'); result_entry.insert(0, password)

generate_button = Button(main_frame, text="Сгенерировать пароль", command=generate_password_action, font=('Arial', 12, 'bold'))
generate_button.pack(pady=15, padx=20, fill="x")

# Фрейм для отображения результата
result_frame = tk.Frame(main_frame)
result_frame.pack(pady=10, padx=20, fill="x")

tk.Label(result_frame, text="Ваш пароль:").pack(side=tk.LEFT, padx=5)
result_entry = Entry(result_frame, font=('Courier New', 12))
result_entry.pack(side=tk.LEFT, fill="x", expand=True, padx=5)

if __name__ == "__main__":
    root.mainloop()
