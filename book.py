class Book:
  # kwargs can also be used to pass if the list of parameteres increases further
  def __init__(self, title, author, isbn, userId=None):
    self.title = title
    self.author = author
    self.isbn = isbn
    self.userId = userId

  def setOwnership(self, owner):
    self.userId = owner

  def revokeOwnernship(self):
    self.userId = None

  def isOwned(self):
    if not self.userId:
      return False
    return True
