import tkinter as tk
from tkinter import font, messagebox

root = tk.Tk()
root.title("계산기")
root.geometry("400x400")

entry = tk.Entry(root, font = font.Font(size =28)) #entry 너비, 글자크기 주기
entry.grid(row = 0, column= 0, columnspan=10)

def btn_click(text):
    # 현재 entry 문자열을 들고와서 변수에 담아둠
    current_text= entry.get()
    # entry를 싹 비워줌
    entry.delete(0, tk.END) # 처음부터 끝까지 다 지움
    # 원래 entry에 들어있던 현재 문자열에 새로운 문자 더함
    current_text += str(text)
    # entry에 더한 문자열을 다시 넣어준다
    entry.insert(0, current_text)

def clear():
    entry.delete(0, tk.END)
def equal_sign():
    try:
        result= eval(entry.get())
    except SyntaxError:
        messagebox.showerror("오류","계산할 수 없습니다.")
        entry.delete(0, tk.END)
    except ZeroDivisionError:
        messagebox.showerror("오류", "0으로 나눌 수 없습니다.")
        entry.delete(0, tk.END)
    else:
        entry.delete(0, tk.END) # 지우고 넣어주어야 해...
        entry.insert(0, str(result))

# eval

btn_list = [(7,1,0), (8,1,1), (9,1,2),("/",1,3),
            (4,2,0),(5,2,1), (6,2,2), ("+",2,3),
            (1,3,0), (2,3,1), (3,3,2), ("-",3,3),
            (0,4,1), ("*",4,2)
            ]
# 튜플 언패킹
# a,b,c = colors
# print(a,b,c)

for (text,row,col) in btn_list:
    tk.Button(root, text= text, font = font.Font(size =28), command= lambda t=text:btn_click(t)).grid(row= row, column= col, ipadx=20)
tk.Button(root, text= "C", font = font.Font(size =28), command= clear).grid(row= 4, column= 0, ipadx=20)
tk.Button(root, text= "=", font = font.Font(size =28), command = equal_sign).grid(row= 4, column= 3, ipadx=20)
root.mainloop()
