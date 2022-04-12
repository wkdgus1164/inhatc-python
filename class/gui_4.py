import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def click_next():
    global idx
    idx = idx + 1
    if idx > 2:
        idx = 0

    p.configure(file=photos[idx])
    # p = tk.PhotoImage(file=photos[idx])
    # lbl_photo.configure(image=p)
    # lbl_photo.image = p


def click_prev():
    global idx
    idx = idx - 1
    if idx < 0:
        idx = 2

    p.configure(file=photos[idx])
    # p = tk.PhotoImage(file=photos[idx])
    # lbl_photo.configure(image=p)
    # lbl_photo.image = p


def pg_down(ev):
    click_next()


def pg_up(ev):
    click_prev()


def click_photo(ev):
    messagebox.showinfo("좌표", f'({ev.x}, {ev.y}')


photos = ["./assets/michael.PNG", "./assets/franklin.PNG", "./assets/trevor.PNG"]
idx = 0

w = tk.Tk()
w.title('포토 뷰어 실습')
w.geometry("500x600")
w.bind("<Prior>", pg_up)
w.bind("Prior", pg_down)

p = tk.PhotoImage(file="./assets/michael.PNG")
lbl_photo = ttk.Label(w, image=p)
lbl_page = ttk.Label(w, text=f'{idx + 1} / {len(photos)}')
btn_next = ttk.Button(w, text="다음 페이지", command=click_next)
btn_prev = ttk.Button(w, text="이전 페이지", command=click_prev)

lbl_photo.bind('<Button>', click_photo)

lbl_photo.grid(row=0, column=0, columnspan=3)
btn_next.grid(row=1, column=2, sticky=tk.EW)
lbl_page.grid(row=1, column=1)
btn_prev.grid(row=1, column=0, sticky=tk.EW)

w.mainloop()

# import tkinter as tk
# from tkinter import ttk
#
#
# def popup():
#     if selected.get() == 0:
#         lbl_display.configure(image=p1)
#     elif selected.get() == 1:
#         lbl_display.configure(image=p2)
#     else:
#         lbl_display.configure(image=p3)
#
#
# w = tk.Tk()
# w.title('체크버튼 실습')
# w.geometry("500x600")
#
# selected = tk.IntVar()
# rb_1 = ttk.Radiobutton(w, text="마이클", command=popup, variable=selected, value=0)
# rb_2 = ttk.Radiobutton(w, text="프랜클린", command=popup, variable=selected, value=1)
# rb_3 = ttk.Radiobutton(w, text="트레버", command=popup, variable=selected, value=2)
#
# p1 = tk.PhotoImage(file="./assets/michael.PNG")
# p2 = tk.PhotoImage(file="./assets/franklin.PNG")
# p3 = tk.PhotoImage(file="./assets/trevor.PNG")
#
# lbl_display = ttk.Label(w, text="선택할 플레이어는?")
# lbl_display.configure(image=p1)
#
# rb_1.grid(row=0, column=0)
# rb_2.grid(row=0, column=1)
# rb_3.grid(row=0, column=2)
# lbl_display.grid(row=1, column=0, columnspan=3)
#
# # lbl_display.pack()
# # rb_1.pack()
# # rb_2.pack()
# # rb_3.pack()
# w.mainloop()
