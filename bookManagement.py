from book import Book
import pandas as pd
import os
import storage


# import loggingSystem
#loggingSystem.setup_logging()
class BookManagement:
  def __init__(self):
    self.bookDict = self.initalizeBooks()
    self.bookPath = os.path.join(os.path.dirname(__file__), "books.csv")
    self.headers = ['isbn', 'title', 'author', 'userId']

  def initalizeBooks(self):
    self.bookDict = {}
    if not os.path.exists(self.bookPath):
      pd.DataFrame(columns=self.headers).to_csv(self.bookPath, index=False)

    bookList = pd.read_csv(self.bookPath)
    for _, row in bookList.iterrows():
      self.bookDict[row['isbn']] = Book(row['title'], row['author'],
                                        row['isbn'], row['userId'])
    return self.bookDict

  def addBook(self, title, author, isbn):
    if self.bookDict[isbn]:
      print("This book already exists")
      return
    newBook = Book(title, author, isbn)
    self.bookDict[isbn] = newBook
    # add book to csv as well
    storage.insertDatatoCSV(self.bookPath, newBook, self.headers)

  def listBooks(self):
    for key, value in self.bookDict.items():
      print(
          f"Name: {value.tiitle}, Author: {value.author}, ISBN: {value.isbn}, UserId: {value.userId"
      )

  def deleteBook(self, deleteDict):
    targetCol = ""
    targetValue = ""
    for key, value in deleteDict.items():
      targetCol = key
      targetValue = value

    targetIsbn = [
        isbn for isbn, book in self.bookDict.items()
        if getattr(book, targetCol) == targetValue
    ]

    for isbn in targetIsbn:
      del self.bookDict[isbn]
    storage.deletetDataFromCSV(self.bookPath, deleteDict)

  def updadeBook(self, updateDict):
    targetIsbn = updateDict['isbn']
    targetBook = self.bookDict[targetIsbn]
    for key, value in updateDict.items():
      targetBook[key] = value
    storage.updateDatatoCSV(self.bookPath, "isbn", updateDict)

  def search(self, searchDict):
    targetCol = ""
    targetValue = ""
    for key, value in searchDict.items():
      targetCol = key
      targetValue = value

    targetIsbn = [
        isbn for isbn, book in self.bookDict.items()
        if getattr(book, targetCol) == targetValue
    ]
    for isbn in targetIsbn:
      print(
          f"Name: {self.bookDict[isbn].title} Author: {self.bookDict[isbn].author} ISBN: {self.bookDict[isbn].isbn} UserId: {self.bookDict[isbn].userId}"
      )
