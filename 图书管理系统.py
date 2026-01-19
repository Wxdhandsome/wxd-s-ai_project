# class Book():
#     def __init__(self,title,author,isbn,is_borrowed):
#         self.title=title
#         self.author=author
#         self.isbn=isbn
#         self.is_borrowed=is_borrowed
#     def borrow_book(self):
#         pass
#     def return_book(self):
#         pass
# class Libirary(Book):
#     def __init__(self,books,title,author,isbn,is_borrowed):
#         super().__init__(title,author,isbn,is_borrowed)
#         self.books=books
#         self.books={}
#     def add_book(self,title,author,sibn,is_borrowed):
#         if title not in self.books:
#             self.books[title]=Book(title,author,sibn,is_borrowed)
#             print('添加成功')
#         else:
#             print(f'{title}已存在')
#     def find_book(self):
#         title=input('请输入你要查询的书籍')
#         if title in self.books:
#             print(f'{title}的作者是：{self.books[title].author},书籍编号是：{self.books[title].isbn}')
#         else:
#             print('没有此书')
#     def borrow_book(self):
#         title=input('请输入你要借的书籍')
#         if title in self.books:
#             if self.books[title].is_borrowed==False:
#                 self.books[title].is_borrowed=True
#                 print('你已成功借出')
#             else:
#                 print('此书已借出')
#         else:
#             print('没有此书')
#     def return_book(self):
#         title=input('请输入你要归还的书籍')
#         if title in self.books:
#             if self.books[title].is_borrowed==True:
#                 self.books[title].is_borrowed=False
#                 print('你已成功归还')
#             else:
#                 print('此书已归还')
#         else:
#             print('没有此书')
#
# lib_1=Libirary({},'《哈利波特》','J.K.罗琳','123456789',False)
# lib_1.add_book('哈利波特','J.K.罗琳','123456789',False)
# lib_1.find_book()
# lib_1.borrow_book()
# lib_1.return_book()
class Book:
    """图书类"""

    def __init__(self, title, author, isbn):
        """
        初始化图书
        :param title: 书名
        :param author: 作者
        :param isbn: ISBN编号
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False  # 默认未借出

    def borrow_book(self):
        """借书操作"""
        if self.is_borrowed:
            print(f"《{self.title}》已被借出")
            return False
        else:
            self.is_borrowed = True
            print(f"成功借阅《{self.title}》")
            return True

    def return_book(self):
        """还书操作"""
        if not self.is_borrowed:
            print(f"《{self.title}》未被借出")
            return False
        else:
            self.is_borrowed = False
            print(f"成功归还《{self.title}》")
            return True


class Library:
    """图书馆管理类"""

    def __init__(self):
        """初始化图书馆，创建空的图书列表"""
        self.books = []

    def add_book(self, book):
        """
        添加图书到图书馆
        :param book: Book对象
        """
        self.books.append(book)
        print(f"已添加图书: 《{book.title}》 by {book.author}")

    def find_book_by_title(self, title):
        """
        根据书名查找图书
        :param title: 书名
        :return: 找到的Book对象，如果不存在返回None
        """
        for book in self.books:
            if book.title == title:
                return book
        print(f"未找到书名为《{title}》的图书")
        return None

    def borrow_book(self, title):
        """
        借阅图书
        :param title: 书名
        """
        book = self.find_book_by_title(title)
        if book:
            book.borrow_book()

    def return_book(self, title):
        """
        归还图书
        :param title: 书名
        """
        book = self.find_book_by_title(title)
        if book:
            book.return_book()


# 使用示例
if __name__ == "__main__":
    # 创建图书馆实例
    library = Library()

    # 添加图书
    book1 = Book("Python编程从入门到实践", "Eric Matthes", "978-7-115-46302-6")
    book2 = Book("算法图解", "Aditya Bhargava", "978-7-115-44765-1")
    book3 = Book("深入理解计算机系统", "Randal E. Bryant", "978-7-111-59586-7")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # 借阅图书
    library.borrow_book("Python编程从入门到实践")
    library.borrow_book("算法图解")

    # 再次尝试借阅已借出的图书
    library.borrow_book("Python编程从入门到实践")
    # 归还图书
    library.return_book("Python编程从入门到实践")

    # 尝试借阅不存在的图书
    library.borrow_book("不存在的书")