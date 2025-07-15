# Book 클래스
# 제목과 저자
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def display_info(self):
        print(f"제목: [{self.title}], 저자: [{self.author}]")
    def __del__(self):
        print(f"[{self.title}]의 객체가 소멸되었습니다")

book1 = Book("해리포터","J.K 롤링")
book2 = Book("이방인","알베르카뮈")

book1.display_info()
book2.display_info()