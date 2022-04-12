import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def popup():
    if checked.get() == 0:
        lbl_display.configure(text="체크버튼 OFF")
        messagebox.showinfo("언체크됨", "체크버튼 OFF")
    elif checked.get() == 1:
        lbl_display.configure(text="체크버튼 ON")
        messagebox.showinfo("언체크됨", "체크버튼 ON")
    else:
        messagebox.showerror("오류", "실행될 일 없음")


w = tk.Tk()
w.title('체크버튼 실습')
w.geometry("200x100")

checked = tk.IntVar()
cb_on_off = ttk.Checkbutton(w, text='출석 체크', variable=checked, command=popup)
lbl_display = ttk.Label(w, text="")
btn_dummy = ttk.Button(w, text="더미버튼")

cb_on_off.pack()
lbl_display.pack()
btn_dummy.pack()

w.mainloop()

# import tkinter as tk
# from tkinter import messagebox
#
#
# def popup():
#     messagebox.askyesnocancel("클릭", "버튼이 눌렸습니다.")
#     messagebox.showwarning("클릭", "버튼이 눌렸습니다.")
#     messagebox.showinfo("클릭", "버튼이 눌렸습니다.")
#
#
# w = tk.Tk()
# w.title('세 번째 GUI 프로그램')
#
# p1 = tk.PhotoImage(file="./assets/michael.PNG")
# p2 = tk.PhotoImage(file="./assets/franklin.PNG")
# p3 = tk.PhotoImage(file="./assets/trevor.PNG")
#
# lbl_d1 = tk.Label(w, image=p1)
# lbl_d2 = tk.Label(w, image=p2)
# btn_d3 = tk.Button(w, image=p3, command=popup)
#
# lbl_d1.pack(side="left")
# lbl_d2.pack(side="left")
# btn_d3.pack(side="left")
#
# w.mainloop()
#
# import tkinter as tk
#
# w = tk.Tk()
# w.title('세 번째 GUI 프로그램')
#
# p1 = tk.PhotoImage(file="./assets/michael.PNG")
# p2 = tk.PhotoImage(file="./assets/franklin.PNG")
# p3 = tk.PhotoImage(file="./assets/trevor.PNG")
#
# lbl_d1 = tk.Label(w, image=p1)
# lbl_d2 = tk.Label(w, image=p2)
# btn_d3 = tk.Button(w, image=p3)
#
# lbl_d1.pack(side="left")
# lbl_d2.pack(side="left")
# btn_d3.pack(side="left")
#
# w.mainloop()
#
