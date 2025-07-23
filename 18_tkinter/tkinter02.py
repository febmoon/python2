# 레이아웃 -place와 grid

import tkinter as tk
root = tk.Tk()
root.title("창")
root.geometry("800x600")


### place 사용 - place(x=, y=)
# 이번엔 pack 말고 절대위치인 place를 이용해보자 -> 크기를 변경하면 가려져버린다!~~

# label1 = tk.Label(root, text = "텍스트1")
# label1.place(x=0, y=0)
#
# label2 = tk.Label(root, text = "텍스트2")
# label2.place(x=0, y=200)
#
# label3 = tk.Label(root, text = "텍스트3")
# label3.place(x=300, y=300)
#
# label4 = tk.Label(root, text = "텍스트4")
# label4.place(x=500, y=0)

### grid 사용 - grid(row= , column=)
label1 = tk.Label(root, text = "텍스트1", bg = "blue")
label1.grid(row= 0, column=0)

label2 = tk.Label(root, text = "텍스트2", bg = "yellow")
label2.grid(row=1 , column=0)

label3 = tk.Label(root, text = "텍스트3", bg = "pink")
label3.grid(row=2 , column=0, rowspan=2) # 2행,3행 모두 차지한다

label4 = tk.Label(root, text = "텍스트4", bg = "red")
label4.grid(row= 4, column=0,)

label5 = tk.Label(root, text = "텍스트5", bg = "red")
label5.grid(row= 0, column=1)

label6 = tk.Label(root, text = "텍스트6", bg = "red")
label6.grid(row= 0, column=2)

label7 = tk.Label(root, text = "텍스트7", bg = "red")
label7.grid(row= 2, column=1, columnspan=2) # 1번,2번 열을 모두 차지한다~

label8 = tk.Label(root, text = "텍스트8", bg = "red")
label8.grid(row= 3, column=3)

root.mainloop()