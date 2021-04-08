#tkinter 라이브러리 사용
from tkinter import *

# 이벤트 액션
def event(btn) : 
    # 'C' 를 입력하면 clear 함수 실행
    if btn == 'C': 
        clear()
    # '=' 을 입력하면 이전 내용 삭제 후 계산 하여 결과 값 출력
    elif btn == '=':
        rst = eval(input.get())
        clear()
        insert(0, rst)
    # 'C' 와 '=' 를 제외한 모든 버튼 값 그대로 출력
    else :
        insert(END, btn)

# 입력
def insert(key, val) :
    input.get()
    input.insert(key, val)

# 초기화
def clear() : 
    input.get()
    input.delete(0, END)

# 창 생성 : 타이틀 부여, 속성부여
calc = Tk()
calc.title("calculator")
calc.geometry("270x125")
calc.resizable(False, False)

# 숫자 버튼 생성
buttons = [
    '7', '8', '9', '+', 'C'
    , '4', '5', '6', '-', ' '
    , '1', '2', '3', '*', ' '
    , '0', '00', '.', '=', '/'
]

i = 0
x = 5
for b in buttons:
    btn = Button(calc, text = b, width = x, command = (lambda y = b: event(y)))
    btn.grid(row = i//x+1, column = i%x)
    i += 1

# 환경설정 ( 컬럼크키, 컬럼나열값, 배경색 등)
input = Entry(calc, width = 33, bg = '#D9E5FF')
input.grid(row = 0, column = 0, columnspan = x)

# 프로그램 실행
calc.mainloop()