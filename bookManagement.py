from book import Book
import pandas as pd
import os
import storage
import json
import menuPrinter
# import loggingSystem
#loggingSystem.setup_logging()
class BookManagement:
  def __init__(self):
    self.bookPath = os.path.join(os.path.dirname(__file__), "books.json")
    self.bookDict = self.initalizeBooks()

  def optionsAvailable(self):
    optionfunc = {
      1: self.addBook,
      2: self.deleteBook,
      3: self.updateBook,
      4: self.search,
      5: self.listBooks
    }
    msgList = []
    msgList.append("1: Add")
    msgList.append("2: Delete")
    msgList.append("3: Update")
    msgList.append("4: Search")
    msgList.append("5: List")
    option = int(menuPrinter.getInput(msgList))
    optionfunc[option]()


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


  def addBook(self):
    menuMsg = {
      'isbn': "Enter Book ISBN: ",
      'title': "Enter Book Title: ",
      'author': "Enter Book Author: "
    }
    addDict = menuPrinter.addPrinter(menuMsg)
    title = addDict['title']
    author = addDict['author']
    isbn = addDict['isbn']
    # print(f"Hi this the book {self.bookDict}")
    if isbn in list(self.bookDict.keys()):
      print("This book already exists")
      return
    newBook = Book(title, author, isbn)
    self.bookDict[isbn] = newBook

    targetDict = {}
    for isbn, book in self.bookDict.items():
      tempDict = book.__dict__
      targetDict[isbn] = tempDict
    print(self.bookDict)
    storage.insertDatatoJson(self.bookPath,targetDict)
    print(f"This is book is added: {title}")
  
  # Testeds
  def listBooks(self):
    for key, value in self.bookDict.items():
      print(
          f"Name: {value.title}, Author: {value.author}, ISBN: {value.isbn}, UserId: {value.userId}"
      )

  def deleteBook(self):
    msgList = [
      "Select option based on which delete should work",
      "1: ISBN",
      "2: Title",
      "3: Author"
    ]
    inp = int(menuPrinter.getInput(msgList))
    targetString = menuPrinter.getInput([msgList[inp]])
    deleteDict = {(msgList[inp]).split(':')[1].strip().lower():targetString}

    targetCol = ""
    targetValue = ""
    for key, value in deleteDict.items():
      targetCol = key
      targetValue = value

    targetIsbn = set()
    for isbn, book in self.bookDict.items():
      targetDict = book.__dict__
      for key, value in targetDict.items():
        if key == targetCol and value == targetValue:
          targetIsbn.add(isbn)

    if not targetIsbn:
      print("Nothing is deleted, There is no match")
      return 

    for isbn in targetIsbn:
      del self.bookDict[isbn]
    storage.deletetDataFromJson(self.bookPath, deleteDict)
    print("Successfully delete")

  def updateBook(self):
    menuMsg = {
      'isbn': "Enter Book ISBN: ",
      'title': "Enter updated Book Title: ",
      'author': "Enter updated Book Author: "
    }
    updateDict = menuPrinter.addPrinter(menuMsg)
    targetIsbn = updateDict['isbn']
    targetBook = self.bookDict[targetIsbn]
    for key, value in updateDict.items():
      setattr(targetBook,key,value)
    storage.updateDatatoCSV(self.bookPath, targetIsbn, updateDict)

  def search(self):
    menuMsg ={
      'targetString': "Enter the string or substring you are searching: "
    }
    searchDict = menuPrinter.addPrinter(menuMsg)
    targetString = searchDict['targetString']
    targetIsbn = set()
    for isbn,book in self.bookDict.items():
      targetDict = book.__dict__
      #print(targetDict)
      for key, value in targetDict.items():
        # print(targetString)
        if value and targetString.lower() in value.lower():
          targetIsbn.add(isbn)

    for isbn in targetIsbn:
      print(
          f"Name: {self.bookDict[isbn].title} Author: {self.bookDict[isbn].author} ISBN: {self.bookDict[isbn].isbn} UserId: {self.bookDict[isbn].userId}"
      )
