from bookManagement import BookManagement
import sys

if __name__ == '__main__':
  bookManager = BookManagement()
  #print(bookManager.bookDict)
  while(True):
    bookManager.addBook({"title": "The Great Gatsby",
                      "author": "F. Scott Fitzgerald",
                      "isbn": "978074"})
    bookManager.search("Scott")
    sys.exit(0)
  # bookManager.listBooks()
