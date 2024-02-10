# users = []

# def add_user(name, user_id):
#     users.append({"name": name, "user_id": user_id})
class User:
  def __init__(self, userId, name, books):
    self.userId = userId
    self.name = name