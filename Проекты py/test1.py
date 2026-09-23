import interface.py
ccerwntp = ""
#Change
output_text.insert(END,ceerwntp)
root.caesar_radio.config(command = cc)
root.atbash_radio.config(command = cc)
def cc():
    global ceerwntp,selected_cipher
    ceerwntp = root.selected_cipher.get()
    if selected_cipher == "Цезарь":
        output_text.delete(0,END)
        output_text.insert(END,"Зашифровано шифром Цезаря")
        shift_entry.config(state = "normal")
    elif selected_cipher == "Атбаш":
        output_text.delete(0,END)
        output_text.insert(END,"Зашифровано шифром Атбаш")
        shift_entry.config(state = "disabled")
output_text.insert(END,ceerwntp)
root.caesar_radio.config(command = cc)
root.atbash_radio.config(command = cc)

output_text = tk.Text(output_frame, height=5, width=50, state=tk.DISABLED)
output_text.pack(padx=5, pady=5)
root.choice.set("Цезарь")
cc()
root.mainloop()
