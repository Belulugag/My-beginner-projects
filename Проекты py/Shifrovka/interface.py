import tkinter as tk

root = tk.Tk()
root.title("Шифровальщик текста")

cipher_frame = tk.LabelFrame(root, text="Выберите шифр")
cipher_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

selected_cipher = tk.StringVar(value="Caesar") # Переменная для хранения выбранного шифра

caesar_radio = tk.Radiobutton(cipher_frame, text="Шифр Цезаря", variable=selected_cipher, value="Caesar")
caesar_radio.pack(anchor=tk.W, padx=5, pady=2)

atbash_radio = tk.Radiobutton(cipher_frame, text="Шифр Атбаш", variable=selected_cipher, value="Atbash")
atbash_radio.pack(anchor=tk.W, padx=5, pady=2)

caesar_afine_cipher = tk.Radiobutton(cipher_frame, text="Шифр Цезаря(Афинный)", variable=selected_cipher, value="CAfine")
caesar_afine_cipher.pack(anchor=tk.W, padx=5, pady=2)

#input
input_frame = tk.LabelFrame(root, text="Введите текст")
input_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
input_entry = tk.Entry(input_frame, width=50)
input_entry.pack(padx=5, pady=5)

#shift
shift_frame = tk.LabelFrame(root, text="Сдвиг (для шифра Цезаря)")
shift_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
shift_entry = tk.Entry(shift_frame, width=10)
shift_entry.insert(0, "3") # Значение по умолчанию
shift_entry.pack(padx=5, pady=5)

#select
mode_frame = tk.LabelFrame(root, text="Режим")
mode_frame.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

cipher_mode = tk.StringVar(value="encrypt") # Переменная для режима

encrypt_radio = tk.Radiobutton(mode_frame, text="Шифровать", variable=cipher_mode, value="encrypt")
encrypt_radio.pack(anchor=tk.W, padx=5, pady=2)

decrypt_radio = tk.Radiobutton(mode_frame, text="Дешифровать", variable=cipher_mode, value="decrypt")
decrypt_radio.pack(anchor=tk.W, padx=5, pady=2)

process_button = tk.Button(root, text="Обработать")
process_button.grid(row=4, column=0, padx=10, pady=10)

output_frame = tk.LabelFrame(root, text="Результат")
output_frame.grid(row=5, column=0, padx=10, pady=10, sticky="ew")
output_text = tk.Text(output_frame, height=5, width=50, state=tk.DISABLED) # Поле для вывода, изначально неактивно
output_text.pack(padx=5, pady=5)
