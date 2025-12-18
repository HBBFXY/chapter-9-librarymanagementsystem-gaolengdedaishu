class Book:
    """书籍类，包含书籍属性和借阅相关方法"""
    def __init__(self, title, author, isbn):
        self.title = title  
        self.author = author 
        self.isbn = isbn  
        self.available = True 

    def check_availability(self):
        """检查书籍是否可借"""
        return self.available

    def borrow_book(self):
        """借书操作：将书籍状态改为不可借"""
        if self.available:
            self.available = False
            return True
        return False

    def return_book(self):
        """还书操作：将书籍状态改为可借"""
        self.available = True

    def __str__(self):
        """返回书籍的字符串表示"""
        status = "可借" if self.available else "已借出"
        return f"《{self.title}》（作者：{self.author}，ISBN：{self.isbn}）- {status}"


class User:
    """用户类，包含用户属性和借阅书籍的管理方法"""
    def __init__(self, name, card_id):
        self.name = name 
        self.card_id = card_id 
        self.borrowed_books = [] 

    def borrow_book(self, book):
        """用户借书：将书籍添加到已借列表"""
        if book.borrow_book():
            self.borrowed_books.append(book)
            print(f"\n{self.name} 成功借阅《{book.title}》")
            return True
        else:
            print(f"\n{self.name} 借阅失败：《{book.title}》已被借出")
            return False

    def return_book(self, book):
        """用户还书：将书籍从已借列表移除"""
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"\n{self.name} 成功归还《{book.title}》")
            return True
        else:
            print(f"\n{self.name} 还书失败：未借阅《{book.title}》")
            return False

    def show_borrowed_books(self):
        """显示用户已借的书籍"""
        if not self.borrowed_books:
            print(f"\n{self.name} 目前没有借阅任何书籍")
        else:
            print(f"\n{self.name} 已借书籍：")
            for book in self.borrowed_books:
                print(f"- {book}")

    def __str__(self):
        """返回用户的字符串表示"""
        return f"用户：{self.name}（借书卡号：{self.card_id}），已借书籍数量：{len(self.borrowed_books)}"


class Library:
    """图书馆类，管理书籍和用户，处理借阅/还书请求"""
    def __init__(self, name):
        self.name = name  
        self.books = []  
        self.users = [] 

    def add_book(self, book):
        """添加书籍到图书馆"""
        if book not in self.books:
            self.books.append(book)
            print(f"\n书籍《{book.title}》已添加到{self.name}")
        else:
            print(f"\n书籍《{book.title}》已存在于{self.name}")

    def register_user(self, user):
        """注册用户到图书馆"""
       
        if any(u.card_id == user.card_id for u in self.users):
            print(f"\n注册失败：借书卡号{user.card_id}已被使用")
            return False
        self.users.append(user)
        print(f"\n用户{user.name}（卡号：{user.card_id}）已成功注册到{self.name}")
        return True

    def find_book_by_isbn(self, isbn):
        """根据ISBN查找书籍"""
        for book in self.books:
            if book.isbn == isbn:
                return book
        print(f"\n未找到ISBN为{isbn}的书籍")
        return None

    def find_user_by_card_id(self, card_id):
        """根据借书卡号查找用户"""
        for user in self.users:
            if user.card_id == card_id:
                return user
        print(f"\n未找到借书卡号为{card_id}的用户")
        return None

    def borrow_book(self, card_id, isbn):
        """处理用户借书请求"""
        user = self.find_user_by_card_id(card_id)
        book = self.find_book_by_isbn(isbn)
        if user and book:
            user.borrow_book(book)

    def return_book(self, card_id, isbn):
        """处理用户还书请求"""
        user = self.find_user_by_card_id(card_id)
        book = self.find_book_by_isbn(isbn)
        if user and book:
            user.return_book(book)

    def show_all_books(self):
        """显示图书馆所有书籍"""
        if not self.books:
            print(f"\n{self.name} 目前没有藏书")
        else:
            print(f"\n{self.name} 藏书列表：")
            for book in self.books:
                print(f"- {book}")

    def show_all_users(self):
        """显示图书馆所有注册用户"""
        if not self.users:
            print(f"\n{self.name} 目前没有注册用户")
        else:
            print(f"\n{self.name} 注册用户列表：")
            for user in self.users:
                print(f"- {user}")



if __name__ == "__main__":
   
    city_library = Library("城市图书馆")

  
    book1 = Book("Python编程：从入门到实践", "埃里克·马瑟斯", "9787115428028")
    book2 = Book("算法导论", "托马斯·科尔曼", "9787111407010")
    book3 = Book("数据结构与算法分析", "马克·艾伦·维斯", "9787111641230")
    city_library.add_book(book1)
    city_library.add_book(book2)
    city_library.add_book(book3)

   
    user1 = User("张三", "U001")
    user2 = User("李四", "U002")
    user3 = User("王五", "U001")  # 重复卡号
    city_library.register_user(user1)
    city_library.register_user(user2)
    city_library.register_user(user3)

   
    city_library.show_all_books()
    city_library.show_all_users()

    
    city_library.borrow_book("U001", "9787115428028")  
    city_library.borrow_book("U002", "9787115428028")  
    city_library.borrow_book("U002", "9787111407010") 

  
    user1.show_borrowed_books()
    user2.show_borrowed_books()

   
    city_library.return_book("U001", "9787115428028") 
    city_library.return_book("U002", "9787115428028")  

    
    city_library.show_all_books()# 在这里编写代码
