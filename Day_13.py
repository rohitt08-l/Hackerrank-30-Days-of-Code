from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass
#Write MyBook class
class MyBook(Book):
    def __init__(self,title,author,price):
        super().__init__(title,author)
        self.price=price
    def display(self):
        print('Title:',title)
        print('Author:',author)
        print('Price:',self.price)
title=input("Enter the title of the book: ")
author=input("Enter the author of the book: ")
price=int(input("Enter the price of the book: "))
new_novel=MyBook(title,author,price)
new_novel.display()