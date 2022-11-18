#Association --> Author - Book
class Author:
  def __init__(self, name):
    self.name = name
    self.books = []

  def addBook(self, title, yearPublished):
    self.books.append([title, yearPublished])

class Book:
  def __init__(self, title, year):
    self.title = title
    self.year = year

author_one = Author("Martin, G. R .R")
author_two = Author("Tolkien, J. R. R.")
author_three = Author("Sala S.")
book_one = Book("A game of thrones", 1996)
book_two = Book("A clash of kings", 1998)
book_three = Book("A storm of sword", 2000)
book_four = Book("The fellowship of the ring", 1954)
book_five = Book("The two towers", 1954)
book_six = Book("The return of the king", 1955)

author_one.addBook(book_one.title, book_one.year)
author_one.addBook(book_two.title, book_two.year)
author_one.addBook(book_three.title, book_three.year)
author_two.addBook(book_four.title, book_four.year)
author_two.addBook(book_five.title, book_five.year)
author_two.addBook(book_six.title, book_six.year)


print(author_one.books)
print(author_two.books)
print(author_three.books)