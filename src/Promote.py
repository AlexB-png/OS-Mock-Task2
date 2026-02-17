from components.PythonFunctions.PromoteUser import Promote

user = input("Input the user ID of the new admin user ")
option = input("true : Promote , false : Demote ")

try:
  user = int(user)
  option = option == 'true'
  Promote(user, option)
except ValueError:
  print("Failure!")
