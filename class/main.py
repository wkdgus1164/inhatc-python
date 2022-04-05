import tkinter as tk


def f2c():
    try:
        f = float(en_input.get())
        c = (f - 32.0) * (5.0 / 9.0)
        lbl_temp.configure(text='화씨 {0} 도는 섭씨 {1}도 입니다.'.format(f, round(c, 4)))
    except ValueError as e:
        lbl_temp.configure(text='숫자만 입력해주세요\n{0}'.format(e))
        en_input.delete(0, 'end')


def c2f():
    try:
        c = float(en_input.get())
        f = (c * 9 / 5) + 32

        lbl_temp.configure(text='섭씨 {0} 도는 화씨 {1}도 입니다.'.format(c, round(f, 4)))
    except ValueError as e:
        lbl_temp.configure(text='숫자만 입력해주세요\n{0}'.format(e))
        en_input.delete(0, 'end')


w = tk.Tk()
w.title('두 번째 GUI 프로그램')
w.geometry('300x100')

en_input = tk.Entry(w)
btn_f2c = tk.Button(w, text='화씨 -> 섭씨', command=f2c)
btn_c2f = tk.Button(w, text='섭씨 -> 화씨', command=c2f)
lbl_temp = tk.Label(w, text='온도변환 프로그램')

en_input.pack()
btn_f2c.pack()
btn_c2f.pack()
lbl_temp.pack()

en_input.focus()
w.mainloop()
