import tkinter as tk


def star():
    n = int(en_input.get())
    text = ''
    for i in range(1, n + 1):
        for space in range(n - i, 0, -1):
            text += ' '

        for star in range(1, 2 * i):
            text += '*'
        text += '\n'
    lbl_temp.configure(text=text)


if __name__ == '__main__':
    w = tk.Tk()
    w.title('별찍기 GUI 프로그램')
    w.geometry('300x300')

    en_input = tk.Entry(w)
    btn_f2c = tk.Button(w, text='실행', command=star)
    lbl_temp = tk.Label(w, text='별찍기')

    en_input.pack()
    btn_f2c.pack()
    lbl_temp.pack()

    en_input.focus()
    w.mainloop()
