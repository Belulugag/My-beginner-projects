from tkinter import *
from PIL import Image, EpsImagePlugin
from tkinter import messagebox
import io

EpsImagePlugin.gs_binary = r'C:\Program Files\gs\gs10.07.1\bin\gswin64c.exe'

tk = Tk()
tk.title("Pypaint")

height_cs = 500
width_cs = 700
paint = Canvas(tk, width=width_cs,
               height=height_cs,
               bg="white")

brsz = 3
colour = f"#000000"

brightness_var = IntVar(value=255)

#draw functions
def draw(event):
    global brsz
    global colour
    x1 = event.x - brsz
    x2 = event.x + brsz
    y1 = event.y - brsz
    y2 = event.y + brsz
    paint.create_oval(x1, y1, x2, y2, fill=colour, outline=colour)

def brsz_change(new_size_str):
    global brsz
    brsz = int(new_size_str)

def update_color(value):
    global colour
    red = rscale.get()
    green = gscale.get()
    blue = bscale.get()
    bright = brightness_var.get()

    factor = bright / 255.0
    r_new = int(red * factor)
    g_new = int(green * factor)
    b_new = int(blue * factor)

    r_new = max(0, min(255, r_new))
    g_new = max(0, min(255, g_new))
    b_new = max(0, min(255, b_new))

    color_code = f"#{r_new:02x}{g_new:02x}{b_new:02x}"
    colour = color_code

    colour_var.set(colour)

    color_label.config(bg=colour)

    entry.config(fg=colour)

    entry.config(state="normal")
    entry.delete(0, END)
    entry.insert(0, colour)
    entry.config(state="readonly")

def clear_all():
    paint.delete("all")

paint.bind("<B1-Motion>", draw)

# Использование pack для главного холста
paint.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

#save function
def save_canvas_image(canvas, filename, file_format):
    filename = filename.strip()
    if not filename:
        messagebox.showerror("Ошибка", "Введите имя файла!")
        return

    if not filename.lower().endswith(f".{file_format.lower()}"):
        filename += f".{file_format.lower()}"

    canvas.update_idletasks()
    ps = canvas.postscript(colormode='color')
    img = Image.open(io.BytesIO(ps.encode('utf-8')))
    img.load(scale=2)
    try:
        img.save(filename, format=file_format.upper())
        messagebox.showinfo("Успех", f"Изображение сохранено как {filename}")
    except Exception as e:
        messagebox.showerror("Ошибка сохранения", f"Не удалось сохранить изображение: {e}")

# UI
# Создаем основной фрейм для виджетов управления
controls_frame = Frame(tk)
controls_frame.pack(side=RIGHT, fill=Y, padx=5, pady=5) # Используем pack для основного фрейма

file_name_input = Entry(controls_frame, width=15)
file_name_input.pack(pady = 10,padx = 10)

#file format
file_formats = ["PNG", "JPEG", "JPG", "GIF", "BMP"]
selected_format = StringVar(tk)
selected_format.set(file_formats[0])

format_menu = OptionMenu(controls_frame, selected_format, *file_formats)
format_menu.pack(pady=5, padx=5)

save_button = Button(
    controls_frame,
    text='Сохранить',
    command=lambda: save_canvas_image(paint, file_name_input.get(), selected_format.get())
)
save_button.pack(pady = 5, padx = 5)

razmerscale = Scale(controls_frame, label="Размер кисти", to=50, resolution=1,
                    orient=HORIZONTAL, length=150, width=20, command=brsz_change)
razmerscale.set(brsz)
razmerscale.pack(pady=5, padx=5)

rscale = Scale(controls_frame, label="красный", to=255, resolution=1,
               orient=HORIZONTAL, length=150, width=20,
               activebackground="red", fg="red", command=update_color)
rscale.pack(pady=5, padx=5)

gscale = Scale(controls_frame, label="зелёный", to=255, resolution=1,
               orient=HORIZONTAL, length=150, width=20,
               activebackground="green", fg="green", command=update_color)
gscale.pack(pady=5, padx=5)

bscale = Scale(controls_frame, label="синий", to=255, resolution=1,
               orient=HORIZONTAL, length=150, width=20,
               activebackground="blue", fg="blue",command=update_color)
bscale.pack(pady=5, padx=5)

brightness_scale = Scale(controls_frame, label="Яркость",
                         from_=0, to=255, resolution=1,
                         orient=HORIZONTAL, length=150, width=20,
                         variable=brightness_var, command=update_color)
brightness_scale.set(255)
brightness_scale.pack(pady=5, padx=5)

colour_var = StringVar()
colour_var.set(colour)
entry = Entry(controls_frame, textvariable=colour_var, state="readonly", width=10)
entry.pack(padx=10, pady=10)

# Добавленные элементы UI
RGB = LabelFrame(controls_frame, text="Текущий цвет") # Перемещаем RGB в controls_frame
RGB.pack( pady=10, padx=10, fill=X) # Используем pack и fill=X

color_label = Label(RGB, font=("Arial", 15, "bold"), height=3, width=16, bg="black", fg="white") # Уменьшаем высоту
color_label.pack(pady=5, padx=5)

# Обновляем начальный цвет индикатора
update_color(None)

clear_canvas = Button(controls_frame, text="Удалить всё", command=clear_all) # Перемещаем кнопку в controls_frame
clear_canvas.pack(pady=5, padx=5)
def toggle_theme():
    current_window_bg = tk.cget("bg")

    dark_window_bg = "#222222"
    dark_frame_bg = "#222222"

    light_window_bg = "#f0f0f0"
    light_frame_bg = "#f0f0f0"

    if current_window_bg == light_window_bg:
        # Применяем темную тему
        tk.config(bg=dark_window_bg)
        controls_frame.config(bg=dark_frame_bg)
    else:
        # Применяем светлую тему
        tk.config(bg=light_window_bg)
        controls_frame.config(bg=light_frame_bg)
theme_button = Button(controls_frame, text="Сменить тему", command=toggle_theme)
theme_button.pack(pady=10, padx=10)
def create_new_canvas():
    global paint, height_cs, width_cs
    new_width = width_entry.get()
    new_height = height_entry.get()
    try:
        width_cs = int(new_width)
        height_cs = int(new_height)
        if width_cs < 50 or height_cs < 50:
            messagebox.showerror("Ошибка", "Минимальный размер 50x50")
            return
        paint.destroy()
        paint = Canvas(tk, width=width_cs, height=height_cs, bg="white")

        # Центрируем холст в окне
        paint.pack(side=LEFT, fill=NONE, expand=False, padx=5, pady=5)

        # Устанавливаем координаты для центрирования
        tk.update_idletasks()
        window_width = tk.winfo_width()
        window_height = tk.winfo_height()
        x_pos = (window_width - width_cs) // 2
        y_pos = (window_height - height_cs) // 2
        paint.place(x=x_pos, y=y_pos)
        paint.bind("<B1-Motion>", draw)
        messagebox.showinfo("Успех", f"Холст создан: {width_cs}x{height_cs}")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числа")

width_entry = Entry(controls_frame, width=10)
width_entry.pack(pady=2)
height_entry = Entry(controls_frame, width=10)
height_entry.pack(pady=2)
new_canvas_button = Button(controls_frame, text="Создать холст", command=create_new_canvas)
new_canvas_button.pack(pady=5)


tk.mainloop()
