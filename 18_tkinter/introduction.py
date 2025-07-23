'''
GUI프로그램
gemini cli
- CLI 키보드 명령어로 줄단위 입력 command line interface
- GUI 마우스 - UI, UX - graphic use interface

tkinter\
tk.Tk()- 기본창새엇ㅇ
.title("창의 제목") - 창을 띄웠을때 상단에 표시될 제목
.geometry("가로*세로")
.mainloop() #GUI 실행

위젯
-버튼과 체크버튼(이중택일ex 동의미동의),라디오버튼(다중택일) 다름
- button.command ->함수넣기
- entry는 한줄 text 여러줄

레이아웃
- pack(2nd m/c) - 상대위치지정 - 한방향으로 쌓인다(모두 패킹 -> 불필요공간 없음)
- grid(m/c) - 그리드 위치 지정- 테이블의 지정된 행,열에 놓는다.
-place(rare) - 절대위치지정 - 절대좌표로 설정, 창크기에 따라 변화안함 -> 불편해 -> 사용안해
'''