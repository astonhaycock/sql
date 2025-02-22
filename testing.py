import sqlite3
from queries import *
from datetime import datetime
from read_all import *
from tabulate import tabulate
import os

db = sqlite3.connect('social.db')

def Options():
  print('\n')
  print('1. Create User')
  print('2. Create Account')
  print('3. Post')
  print('4. Delete Post')
  print('5. comment')
  print('6. delete comment')
  print('7. Like')
  print('8. dislike')
  print('9. Follow')
  print('10. Unfollow')
  print('11. Quit')
  return input('Enter your choice: ')



while True:
  choice = int(Options())


  if(choice == 1):
    email = input('Enter email: ')
    first_name = input('Enter first name: ')
    last_name = input('Enter last name: ')
    create_user(db, email, first_name, last_name)






  if choice == 11:
    break