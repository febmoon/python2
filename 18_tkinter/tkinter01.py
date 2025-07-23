# pip install tk (tkinter가 아니다!)
import tkinter as tk

# 기본 창구성
root = tk.Tk() # 새로운 창 생성
root.title("GUI 프로그래밍 실습") #창제목(타이틀)
root.geometry("800x800") # 창 크기(가로 X 세로)(픽셀단위), 곱하기는 영어x로 처리
root.resizable(False,False) # 창크기 조절 가능/불가능 - 가로 세로 둘다 resize하는 것을 막겠다

### 라벨 만들기
#안녕하세요 창
# label = tk.Label(root, text = "안녕하세요", fg = "red", bg = "blue")
# label.pack(side = "top") # top, bottom, left, right

# 라벨에 이름 나이 주소 3가지를 적고 아래에서 위 방향으로 pack
# nameLabel = tk.Label(root, text = "이름:조수진")
# ageLabel = tk.Label(root, text = "나이:26")
# addressLabel = tk.Label(root, text = "주소:부산")
#
# addressLabel.pack(side = "bottom")
# ageLabel.pack(side = "bottom")
# nameLabel.pack(side = "bottom")

###  위젯 - button 만들기
def button_click():
    print("클릭됨")
    root.quit() #창 닫기 : .quit()
button = tk.Button(root, text = "종료", command = button_click ) #콘솔에 클릭됨이라고 찍힌다
button.pack(side = "bottom")

### 위젯 - entry
entry = tk.Entry(root)
entry.pack(side = "top")

### 위젯 - button - 확인 버튼
def chk_button():
    print(entry.get()) # .get() entry 안의 값을 가져오게 됨
    print(text)
    print(chk_var.get()) # check를 하면 1, 안하면 0 출력
    print(radio_var.get()) #라디오바에 넣은 값을 출력
chk_button = tk.Button(root, text = "확인", command  =chk_button, bg = "pink", padx= 5, pady=10)
    # 요소에 여백을 두는 것 2가지 마진(=바깥)과 패딩(안쪽)
chk_button.pack(side ="top")

### 위젯 - text
text = tk.Text(root, wrap = "word")
# wrap = "none" 줄 바꿈 하지 않음 - 옆으로 계속 감
# wrap = "char" 글자 단위로 줄 바꿈(무지정과 동일, 단어 단위가 아님)
    # 참고)로렘입숨(Lorem ipsum) : 표준채우기텍스트, 무의미한 내용이라 내용이 디자인 판단에 방해되지 않음
# wrap = "word" 단어 단위로 줄 바꿈
text.pack(side = "top")

### 위젯 - 체크버튼
chk_var = tk.IntVar()
chk_btn = tk.Checkbutton(root, text = "위 내용에 거짓이 없음을 동의합니다.", variable=chk_var)
chk_btn.pack(side = "bottom")

### 위젯 - 라디오 버튼 text -> 사용자에게 보여지는 내용, value -> 출력되는 내용
radio_var = tk.StringVar()
r1 = tk.Radiobutton(root, text = "옵션1", value = "첫번째 옵션", variable=radio_var)
r2 = tk.Radiobutton(root, text = "옵션2", value = "두번째 옵션", variable=radio_var)
r3 = tk.Radiobutton(root, text = "옵션3", value = "세번째 옵션", variable=radio_var)
r1.pack(side ="top")
r2.pack(side ="top")
r3.pack(side ="top")

root.mainloop() # 창 실행


