import tkinter as tk
import interface as ip
import utils

def update_cipher_ui():
    current_cipher = ip.selected_cipher.get()

    ip.output_text.config(state=tk.NORMAL)
    ip.output_text.delete("1.0", tk.END)

    if current_cipher == "Caesar":
        ip.output_text.insert(tk.END, "Шифр Цезаря")
        ip.shift_entry.config(state="normal")
    elif current_cipher == "Atbash":
        ip.output_text.insert(tk.END, "Шифр Атбаш")
        ip.shift_entry.config(state="disabled") # Атбаш не требует сдвига
    elif current_cipher == "CAfine":
        ip.output_text.insert(tk.END, "Афинный шифр")
        ip.shift_entry.config(state="normal") # Поле для ввода параметра 'b' (или единого значения)

    ip.output_text.config(state=tk.DISABLED)

def process_text():
    input_data = ip.input_entry.get()
    selected_cipher = ip.selected_cipher.get()
    mode = ip.cipher_mode.get()
    result_text = ""

    try:
        if selected_cipher == "Caesar":
            shift_value = int(ip.shift_entry.get())
            result_text = utils.caesar_cipher(input_data, shift_value, mode)
        elif selected_cipher == "CAfine":
            a_param = 5
            b_param = int(ip.shift_entry.get())
            result_text = utils.affine_cipher_caesar(input_data, a_param, b_param, mode)
        elif selected_cipher == "Atbash":
            result_text = utils.atbash_cipher(input_data, mode) 
    except ValueError:
        result_text = "Ошибка: Некорректный ввод. Убедитесь, что сдвиг является числом."
    except Exception as e:
        result_text = f"Произошла ошибка: {e}"
    ip.output_text.config(state=tk.NORMAL)
    ip.output_text.delete("1.0", tk.END)
    ip.output_text.insert(tk.END, result_text)
    ip.output_text.config(state=tk.DISABLED)

# Привязка команд к радиокнопкам выбора шифра
ip.caesar_radio.config(command=update_cipher_ui)
ip.atbash_radio.config(command=update_cipher_ui)
ip.caesar_afine_cipher.config(command=update_cipher_ui)

# Привязка команды к кнопке "Обработать"
ip.process_button.config(command=process_text)

update_cipher_ui()

ip.root.mainloop()
