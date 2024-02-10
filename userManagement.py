from book import Book
from user import User
import pandas as pd
import os
import storage
import json

class UserManagement:
  def __init__(self):
    self.headers = ['userid', 'name', 'books']
    self.userPath = os.path.join(os.path.dirname(__file__), "users.json")
    self.userDict = self._intiailizeUser()

  def _intiailizeUser(self):
    self.userDict = {}
    if not os.path.exists(self.userPath):
      with open(self.userPath, 'w') as file:
        json.dump(self.userDict,file)

    with open(self.userPath, 'r') as file:
      self.userDict = json.load(file)
    
    userObjDict = {}
    for key, value in self.userDict.items():
      userBooks = [Book(**book) for book in value.get('books', [])]
      userObj = User(userId=value['userId'], name=value['name'], userbooks=value['books'])
      userObjDict[key] = userObj

    return userObjDict

  def listUser(self):
    pass

  def addUser(self, userData):
    userid = userData['userid']
    name = userData['name']
    books = userData.get('books', [])

    if userid in list(self.userDict.keys()):
      print("This user already exists")
      return
    
    userBooks = [Book(**book) if not isinstance(book, Book) else book for book in books]

    newUser = User(userid, name, userBooks)
    self.userDict[userid] = newUser

    booksData = [book.__dict__ for book in userBooks]

    tempDict = {
            userid: {
                "name": name,
                "books": booksData
            }
        }
    storage.insertDatatoJson(self.userPath, tempDict)
    print(f"User added: {name}")

  def deleteUser(self, name, user_id):
    pass
  def searchUser(self, name, user_id):
    pass
  def updateUser(self, name, user_id):
    pass