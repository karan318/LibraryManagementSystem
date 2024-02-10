from userManagement import UserManagement
import sys

if __name__ == '__main__':
  userManager = UserManagement()
  #print(bookManager.bookDict)
  while(True):
    userManager.addUser({"userid": "1",
                      "name": "Manas ",
                      "books": [
                        {"title": "The Great Gatsby",
                      "author": "F. Scott Fitzgerald",
                      "isbn": "978074"},
                      {"title": "The Great Gatsby 2",
                      "author": "F. Scott Fietzgerald",
                      "isbn": "978075"}
                      ]})
    sys.exit(0)
  # bookManager.listBooks()
