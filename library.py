from bookManagement import BookManagement
from userManagement import UserManagement
import menuPrinter
import sys

class Library:
  def __init__(self):
    self.bookManager = BookManagement()
  
  def mainMenu(self):
    optionfunc = {
      1: self.bookManager,
      #2: self.userManager
    }
    msgList = []
    msgList.append("Main menu")
    msgList.append("1: Book Manager")
    msgList.append("2: User Manager")
    msgList.append("3: Services Manager")
    
    # sys.exit(0)
    manager = menuPrinter.getInput(msgList, optionfunc)
    print(manager.bookDict)
    # sys.exit(0)
    manager.optionsAvailable()

if __name__ == '__main__':
  library = Library()
  library.mainMenu()



    
  