from book import Book
import pandas as pd
import os
import storage
import json

# import loggingSystem
#loggingSystem.setup_logging()
class BookManagement:
  def __init__(self):
    self.headers = ['isbn', 'title', 'author', 'userId']
    self.bookPath = os.path.join(os.path.dirname(__file__), "books.json")
    self.bookDict = self.initalizeBooks()

  def initalizeBooks(self):
    self.bookDict = {}
    if not os.path.exists(self.bookPath):
      with open(self.bookPath, 'w') as file:
        json.dump(self.bookDict,file)

    with open(self.bookPath, 'r') as file:
      self.bookDict = json.load(file)

    bookObjDict = {}
    for key, value in self.bookDict.items():
      bookObj = Book(isbn=value['isbn'],title=value['title'],author=value['author'],userId=value['userId'])
      bookObjDict[key] = bookObj

    return bookObjDict


  def addBook(self, addDict):
    title = addDict['title']
    author = addDict['author']
    isbn = addDict['isbn']
    # print(f"Hi this the book {self.bookDict}")
    if isbn in list(self.bookDict.keys()):
      print("This book already exists")
      return
    newBook = Book(title, author, isbn)
    self.bookDict[isbn] = newBook

    tempDict ={ isbn: 
               {
                 "title": title,
                 "author": author,
                 "isbn": isbn,
                 "userId": None
                }
              }

    storage.insertDatatoJson(self.bookPath,tempDict)
    print(f"This is book is added: {title}")
  
  # Tested
  def listBooks(self):
    for key, value in self.bookDict.items():
      print(
          f"Name: {value.title}, Author: {value.author}, ISBN: {value.isbn}, UserId: {value.userId}"
      )

  def deleteBook(self, deleteDict):
    targetCol = ""
    targetValue = ""
    for key, value in deleteDict.items():
      targetCol = key
      targetValue = value

    targetIsbn = []
    for isbn, book in self.bookDict.items():
      targetDict = book.__dict__
      for key, value in targetDict.items():
        if key == targetCol and value == targetValue:
          targetIsbn.append(isbn)

    for isbn in targetIsbn:
      del self.bookDict[isbn]
    storage.deletetDataFromJson(self.bookPath, deleteDict)

  def updateBook(self, updateDict):
    targetIsbn = updateDict['isbn']
    targetBook = self.bookDict[targetIsbn]
    for key, value in updateDict.items():
      setattr(targetBook,key,value)
    storage.updateDatatoCSV(self.bookPath, targetIsbn, updateDict)

  def search(self, targetString):
    targetIsbn = []
    for isbn,book in self.bookDict.items():
      targetDict = book.__dict__
      #print(targetDict)
      for key, value in targetDict.items():
        print(value)
        # print(targetString)
        if value and targetString.lower() in value.lower():
          targetIsbn.append(isbn)

    for isbn in targetIsbn:
      print(
          f"Name: {self.bookDict[isbn].title} Author: {self.bookDict[isbn].author} ISBN: {self.bookDict[isbn].isbn} UserId: {self.bookDict[isbn].userId}"
      )
