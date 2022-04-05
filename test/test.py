import tkinter as tk
import random

alcohol_foods = {
    '맥주': ['치킨', 20000],
    '와인': ['치즈', 5000],
    '고량주': ['짬뽕', 8000],
    '소주': ['골뱅이소면', 9000],
}

file = open('bill.txt', 'w')


def execute():
    input = menu_input.get()
    lbl_recommend.configure(text='')

    if input in alcohol_foods:
        lbl_recommend.configure(text='{0}를 추천합니다. 안주는 {1}~~'.format(input, alcohol_foods[input][0]))
        file.write('{0} 입력 : {1}을 추천합니다. 안주는 {2}~~ 안주가격은 {3}원\n'.format(input, input, alcohol_foods[input][0],
                                                                        alcohol_foods[input][1]))
    elif input == '아무거나':
        array = ['맥주', '와인', '고량주', '소주']
        input = random.choice(array)
        lbl_recommend.configure(
            text='{0}를 추천합니다. 안주는 {1}~~ 안주가격은 {2}원'.format(input, alcohol_foods[input][0], alcohol_foods[input][1]))
        file.write('아무거나 입력 : {0}을 추천합니다. 안주는 {1}~~ 안주가격은 {2}원\n'.format(input, alcohol_foods[input][0],
                                                                         alcohol_foods[input][1]))
    else:
        lbl_recommend.configure(text='{0}는 판매하지 않습니다. 메뉴에서 골라주세요~'.format(input))
        file.write('{0}는 판매하지 않습니다. 메뉴에서 골라주세요~'.format(input))


w = tk.Tk()
w.title('별찍기 GUI 프로그램')
w.geometry('300x300')

lbl_ask = tk.Label(w, text='주문하실 술(맥주/와인/소주/고량주/아무거나/결제)은?')
lbl_recommend = tk.Label(w, text='')
menu_input = tk.Entry(w)
btn_execute = tk.Button(w, text='실행', command=execute)

lbl_ask.pack()
lbl_recommend.pack()
menu_input.pack()
btn_execute.pack()

menu_input.focus()
w.mainloop()
