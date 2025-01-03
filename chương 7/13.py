import tkinter as tk
from tkinter import messagebox

def show_message(chapter, exercise):
    title = f"Chương {chapter}"
    content = f"Lập trình hướng đối tượng với nội dung {exercise}"
    messagebox.showinfo(title, content)

root = tk.Tk()
root.title("Hệ thống bài tập nâng cao")

menu = tk.Menu(root)
root.config(menu=menu)

for chapter in range(1, 8):
    chapter_menu = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label=f"Chương {chapter}", menu=chapter_menu)
    for exercise in range(1, 6):  # Mỗi chương có 5 bài tập
        chapter_menu.add_command(
            label=f"Bài tập {exercise}",
            command=lambda c=chapter, e=exercise: show_message(c, f"Bài tập {e}")
        )

root.mainloop()
