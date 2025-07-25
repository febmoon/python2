import tkinter as tk
from tkinter import messagebox #tk.messagbox라고 안쓰고 바로 messagebox라고 쓸 수 있어

root = tk.Tk()
root.title("회원가입")
root.geometry("500x200")

id_label = tk.Label(root, text="아이디:")
id_label.grid(row=0, column=0, pady=10)

id_entry = tk.Entry(root)
id_entry.grid(row=0, column=1, pady=5)

# entry 옆에 버튼 하나 만들고 해당 버튼 클릭시
# 아이디 출력

def dupl_click():
    # 실제 서버와 데이터베이스에 정보를 요청해서
    # 비교 후에 중복확인 절차 진행
    if id_entry.get() == "":
        messagebox.showwarning("경고","아이디를 입력해주세요")
    else:
        messagebox.showinfo("중복확인", "중복확인이 되었습니다.") # 첫번째 인자 창이름

dupl_button = tk.Button(root,text = "중복확인", command=dupl_click)
dupl_button.grid(row=0, column=2)


password_label = tk.Label(root, text="비밀번호:")
password_label.grid(row=1, column=0)

password_entry = tk.Entry(root, show ="*")
password_entry.grid(row=1, column=1, padx=5)

password_label2 = tk.Label(root, text="비밀번호 확인:")
password_label2.grid(row=2, column=0)

password_entry2 = tk.Entry(root, show ="*")
password_entry2.grid(row=2, column=1, padx=5)

chk_var = tk.IntVar()
chk_box = tk.Checkbutton(root, text= "위 약관 내용에 동의합니다.", variable = chk_var)
chk_box.grid(row=3, column =1)

def signup_click():
    if password_entry.get() != password_entry2.get():  # 일치 동의
        messagebox.showerror("경고", "비밀번호가 일치하지 않습니다.")
    elif chk_var.get() == 0:
        messagebox.showwarning("약관동의", "약관동의가 필요합니다.")
    else:
        messagebox.showinfo("회원가입 완료", "회원가입이 완료되었습니다")

signup_btn = tk.Button(root, text ="회원가입", command=signup_click)
signup_btn.grid(row=4, column=2)
root.mainloop()